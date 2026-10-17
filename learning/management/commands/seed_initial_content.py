import json
from pathlib import Path
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from learning.models import Subject, Topic, Capsule

ALLOWED_MODELS = {
    'learning.subject',
    'learning.topic',
    'learning.capsule',
}

EXPECTED_SUBJECT_COUNT = 5
EXPECTED_TOPIC_COUNT = 5
EXPECTED_CAPSULE_COUNT = 50


class Command(BaseCommand):
    help = (
        "Safely seeds initial learning content (Subjects, Topics, Capsules) "
        "from learning/fixtures/initial_content.json if the database contains no existing content."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--check-only',
            action='store_true',
            help='Validate fixture and database status without writing any data.',
        )

    def handle(self, *args, **options):
        check_only = options.get('check_only', False)

        # 1. Inspect existing content in target database
        existing_subjects = Subject.objects.count()
        existing_topics = Topic.objects.count()
        existing_capsules = Capsule.objects.count()

        if existing_subjects > 0 or existing_topics > 0 or existing_capsules > 0:
            self.stdout.write(
                self.style.WARNING(
                    f"Seeding skipped: database already contains learning content "
                    f"({existing_subjects} subjects, {existing_topics} topics, {existing_capsules} capsules). "
                    f"Existing content is preserved."
                )
            )
            return

        # 2. Locate and load fixture file
        fixture_path = Path(settings.BASE_DIR) / 'learning' / 'fixtures' / 'initial_content.json'
        if not fixture_path.exists():
            raise CommandError(f"Initial content fixture not found at expected path: {fixture_path}")

        try:
            with open(fixture_path, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
        except Exception as e:
            raise CommandError(f"Failed to read or parse fixture JSON: {e}")

        if not isinstance(data, list):
            raise CommandError(f"Fixture root must be a JSON array, got {type(data).__name__}")

        # 3. Validate fixture structure, permitted models, and privacy constraints
        subjects_data = []
        topics_data = []
        capsules_data = []

        for index, item in enumerate(data):
            if not isinstance(item, dict):
                raise CommandError(f"Fixture entry #{index} is not a valid JSON object.")

            model_name = item.get('model')
            if model_name not in ALLOWED_MODELS:
                raise CommandError(
                    f"Forbidden or unexpected model '{model_name}' in fixture entry #{index}. "
                    f"Allowed models: {sorted(ALLOWED_MODELS)}"
                )

            pk = item.get('pk')
            fields = item.get('fields')

            if pk is None or not isinstance(fields, dict):
                raise CommandError(f"Entry #{index} ({model_name}) is missing valid 'pk' or 'fields'.")

            if model_name == 'learning.subject':
                # Critical privacy safeguard: ensure no user subscriber references exist
                subscribers = fields.get('subscribers', [])
                if subscribers:
                    raise CommandError(
                        f"Security violation in Subject #{pk}: 'subscribers' field must be empty. "
                        f"Found {len(subscribers)} user references."
                    )
                subjects_data.append(item)
            elif model_name == 'learning.topic':
                topics_data.append(item)
            elif model_name == 'learning.capsule':
                capsules_data.append(item)

        # Validate expected record counts
        if len(subjects_data) != EXPECTED_SUBJECT_COUNT:
            raise CommandError(
                f"Fixture subject count mismatch: found {len(subjects_data)}, expected {EXPECTED_SUBJECT_COUNT}."
            )
        if len(topics_data) != EXPECTED_TOPIC_COUNT:
            raise CommandError(
                f"Fixture topic count mismatch: found {len(topics_data)}, expected {EXPECTED_TOPIC_COUNT}."
            )
        if len(capsules_data) != EXPECTED_CAPSULE_COUNT:
            raise CommandError(
                f"Fixture capsule count mismatch: found {len(capsules_data)}, expected {EXPECTED_CAPSULE_COUNT}."
            )

        # Validate relational integrity (foreign keys)
        subject_pks = {s['pk'] for s in subjects_data}
        topic_pks = {t['pk'] for t in topics_data}

        for t in topics_data:
            subj_fk = t['fields'].get('subject')
            if subj_fk not in subject_pks:
                raise CommandError(
                    f"Topic #{t['pk']} references non-existent Subject #{subj_fk}."
                )

        for c in capsules_data:
            topic_fk = c['fields'].get('topic')
            if topic_fk not in topic_pks:
                raise CommandError(
                    f"Capsule #{c['pk']} references non-existent Topic #{topic_fk}."
                )

        if check_only:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Validation check passed: fixture contains valid and isolated content "
                    f"({len(subjects_data)} subjects, {len(topics_data)} topics, {len(capsules_data)} capsules)."
                )
            )
            return

        # 4. Atomic database population
        try:
            with transaction.atomic():
                # Populate Subjects
                for item in sorted(subjects_data, key=lambda x: x['pk']):
                    f = item['fields']
                    Subject.objects.create(
                        pk=item['pk'],
                        name=f['name'],
                        description=f.get('description'),
                        icon_class=f.get('icon_class'),
                    )

                # Populate Topics
                for item in sorted(topics_data, key=lambda x: x['pk']):
                    f = item['fields']
                    Topic.objects.create(
                        pk=item['pk'],
                        subject_id=f['subject'],
                        title=f['title'],
                        order=f.get('order', 0),
                    )

                # Populate Capsules
                for item in sorted(capsules_data, key=lambda x: x['pk']):
                    f = item['fields']
                    Capsule.objects.create(
                        pk=item['pk'],
                        topic_id=f['topic'],
                        title=f['title'],
                        front_content=f['front_content'],
                        back_content=f['back_content'],
                        order=f.get('order', 0),
                    )

                # Post-load verification
                created_subjects = Subject.objects.count()
                created_topics = Topic.objects.count()
                created_capsules = Capsule.objects.count()

                if (
                    created_subjects != EXPECTED_SUBJECT_COUNT
                    or created_topics != EXPECTED_TOPIC_COUNT
                    or created_capsules != EXPECTED_CAPSULE_COUNT
                ):
                    raise CommandError(
                        f"Post-seed verification mismatch: created "
                        f"{created_subjects} subjects, {created_topics} topics, {created_capsules} capsules."
                    )

        except Exception as e:
            raise CommandError(f"Database transaction failed during content seeding: {e}")

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded initial learning content: "
                f"{created_subjects} subjects, {created_topics} topics, {created_capsules} capsules."
            )
        )

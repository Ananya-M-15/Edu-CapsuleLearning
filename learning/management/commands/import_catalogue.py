import json
from pathlib import Path
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from learning.models import Subject, Topic, Capsule, QuizQuestion


class Command(BaseCommand):
    help = (
        "Safely and idempotently imports or inspects the course catalogue "
        "from a JSON manifest without duplicating records, destroying progress, "
        "or silently overwriting existing courses, capsules, or quiz questions."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--check-only',
            action='store_true',
            help='Perform read-only validation of manifest and report planned creations and conflicts without modifying the database.',
        )
        parser.add_argument(
            '--fixture',
            type=str,
            default='learning/fixtures/expanded_content.json',
            help='Path to the content manifest JSON file relative to project root or absolute path.',
        )
        parser.add_argument(
            '--overwrite-conflicts',
            action='store_true',
            default=False,
            help='Explicitly overwrite conflicting content on existing records. By default, existing content is preserved.',
        )

    def validate_manifest(self, courses_data):
        """
        Validates the complete manifest structure, course/topic/capsule hierarchy,
        required fields, and quiz answer constraints prior to any database interaction.
        """
        if not isinstance(courses_data, list):
            raise CommandError(f"Catalogue manifest root must be a JSON array, got {type(courses_data).__name__}.")
        if len(courses_data) == 0:
            raise CommandError("Catalogue manifest cannot be empty.")

        seen_subjects = set()
        for c_idx, c in enumerate(courses_data, 1):
            if not isinstance(c, dict):
                raise CommandError(f"Course #{c_idx} must be a dictionary.")
            name = c.get('name')
            if not name or not isinstance(name, str) or not name.strip():
                raise CommandError(f"Course #{c_idx} is missing a valid 'name' string.")
            name = name.strip()
            if name in seen_subjects:
                raise CommandError(f"Duplicate course name '{name}' defined in manifest.")
            seen_subjects.add(name)

            topics = c.get('topics')
            if not isinstance(topics, list) or len(topics) == 0:
                raise CommandError(f"Course '{name}' must define a non-empty 'topics' list.")

            seen_topics = set()
            for t_idx, t in enumerate(topics, 1):
                if not isinstance(t, dict):
                    raise CommandError(f"Course '{name}', Topic #{t_idx} must be a dictionary.")
                title = t.get('title')
                if not title or not isinstance(title, str) or not title.strip():
                    raise CommandError(f"Course '{name}', Topic #{t_idx} is missing a valid 'title'.")
                title = title.strip()
                if title in seen_topics:
                    raise CommandError(f"Course '{name}' has duplicate topic title '{title}'.")
                seen_topics.add(title)

                order = t.get('order', 0)
                if not isinstance(order, int) or order < 0:
                    raise CommandError(f"Topic '{title}' in Course '{name}' has invalid order '{order}'. Must be non-negative integer.")

                capsules = t.get('capsules')
                if not isinstance(capsules, list) or len(capsules) == 0:
                    raise CommandError(f"Course '{name}', Topic '{title}' must define a non-empty 'capsules' list.")

                seen_capsules = set()
                for cap_idx, cap in enumerate(capsules, 1):
                    if not isinstance(cap, dict):
                        raise CommandError(f"Topic '{title}', Capsule #{cap_idx} must be a dictionary.")
                    cap_title = cap.get('title')
                    if not cap_title or not isinstance(cap_title, str) or not cap_title.strip():
                        raise CommandError(f"Topic '{title}', Capsule #{cap_idx} is missing a valid 'title'.")
                    cap_title = cap_title.strip()
                    if cap_title in seen_capsules:
                        raise CommandError(f"Topic '{title}' has duplicate capsule title '{cap_title}'.")
                    seen_capsules.add(cap_title)

                    front = cap.get('front_content')
                    back = cap.get('back_content')
                    if not front or not isinstance(front, str) or not front.strip():
                        raise CommandError(f"Capsule '{cap_title}' in Topic '{title}' is missing 'front_content'.")
                    if not back or not isinstance(back, str) or not back.strip():
                        raise CommandError(f"Capsule '{cap_title}' in Topic '{title}' is missing 'back_content'.")

                    cap_order = cap.get('order', 0)
                    if not isinstance(cap_order, int) or cap_order < 0:
                        raise CommandError(f"Capsule '{cap_title}' in Topic '{title}' has invalid order '{cap_order}'. Must be non-negative integer.")

                    quiz = cap.get('quiz')
                    if quiz is not None:
                        if not isinstance(quiz, dict):
                            raise CommandError(f"Quiz for Capsule '{cap_title}' must be a dictionary.")
                        required_fields = ['prompt', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'explanation']
                        for q_fld in required_fields:
                            val = quiz.get(q_fld)
                            if not val or not isinstance(val, str) or not val.strip():
                                raise CommandError(f"Quiz for Capsule '{cap_title}' is missing required string field '{q_fld}'.")
                        correct_opt = quiz.get('correct_option', '').strip().upper()
                        if correct_opt not in ('A', 'B', 'C', 'D'):
                            raise CommandError(
                                f"Quiz for Capsule '{cap_title}' has invalid correct_option '{quiz.get('correct_option')}'. "
                                f"Must be one of 'A', 'B', 'C', or 'D'."
                            )

    def inspect_catalogue(self, courses_data):
        """
        Performs a strictly read-only inspection of the active database against the manifest.
        Returns planned creations, existing matching records, and all detected content conflicts.
        """
        planned = {'subjects': 0, 'topics': 0, 'capsules': 0, 'quizzes': 0}
        existing = {'subjects': 0, 'topics': 0, 'capsules': 0, 'quizzes': 0}
        conflicts = []

        for c in courses_data:
            name = c['name'].strip()
            desc = c.get('description', '')
            icon = c.get('icon_class', 'fas fa-graduation-cap')

            subj = Subject.objects.filter(name=name).first()
            if not subj:
                planned['subjects'] += 1
            else:
                existing['subjects'] += 1
                subj_diffs = []
                if (subj.description or '') != (desc or ''):
                    subj_diffs.append('description')
                if (subj.icon_class or '') != (icon or ''):
                    subj_diffs.append('icon_class')
                if subj_diffs:
                    conflicts.append(f"Subject '{name}': existing {', '.join(subj_diffs)} differs from manifest.")

            for t in c.get('topics', []):
                t_title = t['title'].strip()
                t_order = t.get('order', 0)

                topic = None
                if subj:
                    topic = Topic.objects.filter(subject=subj, title=t_title).first()

                if not topic:
                    planned['topics'] += 1
                else:
                    existing['topics'] += 1
                    if topic.order != t_order:
                        conflicts.append(
                            f"Topic '{name} -> {t_title}': existing order ({topic.order}) differs from manifest ({t_order})."
                        )

                for cap in t.get('capsules', []):
                    cap_title = cap['title'].strip()
                    front = cap['front_content']
                    back = cap['back_content']
                    cap_order = cap.get('order', 0)

                    capsule = None
                    if topic:
                        capsule = Capsule.objects.filter(topic=topic, title=cap_title).first()

                    if not capsule:
                        planned['capsules'] += 1
                    else:
                        existing['capsules'] += 1
                        cap_diffs = []
                        if capsule.front_content != front:
                            cap_diffs.append('front_content')
                        if capsule.back_content != back:
                            cap_diffs.append('back_content')
                        if capsule.order != cap_order:
                            cap_diffs.append('order')
                        if cap_diffs:
                            conflicts.append(
                                f"Capsule '{name} -> {t_title} -> {cap_title}': existing {', '.join(cap_diffs)} differs from manifest."
                            )

                    q_data = cap.get('quiz')
                    if q_data:
                        if not capsule:
                            planned['quizzes'] += 1
                        else:
                            quiz_q = QuizQuestion.objects.filter(capsule=capsule, prompt=q_data['prompt']).first()
                            if not quiz_q:
                                alt_quiz = QuizQuestion.objects.filter(capsule=capsule).first()
                                if alt_quiz:
                                    existing['quizzes'] += 1
                                    conflicts.append(
                                        f"Quiz on Capsule '{cap_title}': Existing question prompt differs from manifest prompt."
                                    )
                                else:
                                    planned['quizzes'] += 1
                            else:
                                existing['quizzes'] += 1
                                q_diffs = []
                                for fld in ['option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'explanation']:
                                    expected = q_data[fld].strip().upper() if fld == 'correct_option' else q_data[fld]
                                    if getattr(quiz_q, fld) != expected:
                                        q_diffs.append(fld)
                                if (quiz_q.kids_hint or '') != (q_data.get('kids_hint') or ''):
                                    q_diffs.append('kids_hint')
                                if q_diffs:
                                    conflicts.append(
                                        f"Quiz on Capsule '{cap_title}': Existing question differs in {', '.join(q_diffs)}."
                                    )

        return planned, existing, conflicts

    def import_catalogue(self, courses_data, overwrite_conflicts=False):
        """
        Imports courses, topics, capsules, and quizzes atomically.
        If a record already exists with identical content, skips without duplicating.
        If content conflicts, reports the conflict clearly and preserves the existing database record
        unless --overwrite-conflicts is explicitly requested.
        """
        stats = {
            'subjects_created': 0,
            'subjects_existing': 0,
            'topics_created': 0,
            'topics_existing': 0,
            'capsules_created': 0,
            'capsules_existing': 0,
            'quizzes_created': 0,
            'quizzes_existing': 0,
        }
        conflicts = []

        with transaction.atomic():
            for c in courses_data:
                name = c['name'].strip()
                desc = c.get('description', '')
                icon = c.get('icon_class', 'fas fa-graduation-cap')

                subject = Subject.objects.filter(name=name).first()
                if not subject:
                    subject = Subject.objects.create(name=name, description=desc, icon_class=icon)
                    stats['subjects_created'] += 1
                else:
                    stats['subjects_existing'] += 1
                    subj_diffs = []
                    if (subject.description or '') != (desc or ''):
                        subj_diffs.append('description')
                    if (subject.icon_class or '') != (icon or ''):
                        subj_diffs.append('icon_class')
                    if subj_diffs:
                        msg = f"Subject '{name}': existing {', '.join(subj_diffs)} differs from manifest."
                        conflicts.append(msg)
                        if overwrite_conflicts:
                            subject.description = desc
                            subject.icon_class = icon
                            subject.save(update_fields=['description', 'icon_class'])
                            self.stdout.write(self.style.NOTICE(f"  [OVERWRITTEN] Updated Subject '{name}'."))
                        else:
                            self.stdout.write(self.style.WARNING(f"  [CONFLICT] {msg} (Preserved existing)"))

                for t in c.get('topics', []):
                    t_title = t['title'].strip()
                    t_order = t.get('order', 0)

                    topic = Topic.objects.filter(subject=subject, title=t_title).first()
                    if not topic:
                        topic = Topic.objects.create(subject=subject, title=t_title, order=t_order)
                        stats['topics_created'] += 1
                    else:
                        stats['topics_existing'] += 1
                        if topic.order != t_order:
                            msg = f"Topic '{subject.name} -> {t_title}': existing order ({topic.order}) differs from manifest ({t_order})."
                            conflicts.append(msg)
                            if overwrite_conflicts:
                                topic.order = t_order
                                topic.save(update_fields=['order'])
                                self.stdout.write(self.style.NOTICE(f"  [OVERWRITTEN] Updated Topic '{t_title}'."))
                            else:
                                self.stdout.write(self.style.WARNING(f"  [CONFLICT] {msg} (Preserved existing)"))

                    for cap in t.get('capsules', []):
                        cap_title = cap['title'].strip()
                        front = cap['front_content']
                        back = cap['back_content']
                        cap_order = cap.get('order', 0)

                        capsule = Capsule.objects.filter(topic=topic, title=cap_title).first()
                        if not capsule:
                            capsule = Capsule.objects.create(
                                topic=topic,
                                title=cap_title,
                                front_content=front,
                                back_content=back,
                                order=cap_order,
                            )
                            stats['capsules_created'] += 1
                        else:
                            stats['capsules_existing'] += 1
                            cap_diffs = []
                            if capsule.front_content != front:
                                cap_diffs.append('front_content')
                            if capsule.back_content != back:
                                cap_diffs.append('back_content')
                            if capsule.order != cap_order:
                                cap_diffs.append('order')
                            if cap_diffs:
                                msg = f"Capsule '{subject.name} -> {topic.title} -> {cap_title}': existing {', '.join(cap_diffs)} differs from manifest."
                                conflicts.append(msg)
                                if overwrite_conflicts:
                                    capsule.front_content = front
                                    capsule.back_content = back
                                    capsule.order = cap_order
                                    capsule.save(update_fields=['front_content', 'back_content', 'order'])
                                    self.stdout.write(self.style.NOTICE(f"  [OVERWRITTEN] Updated Capsule '{cap_title}'."))
                                else:
                                    self.stdout.write(self.style.WARNING(f"  [CONFLICT] {msg} (Preserved existing)"))

                        q_data = cap.get('quiz')
                        if q_data:
                            quiz_q = QuizQuestion.objects.filter(capsule=capsule, prompt=q_data['prompt']).first()
                            if not quiz_q:
                                alt_quiz = QuizQuestion.objects.filter(capsule=capsule).first()
                                if alt_quiz:
                                    msg = (
                                        f"Quiz on Capsule '{cap_title}': Existing question prompt differs from manifest prompt. "
                                        f"Existing: '{alt_quiz.prompt[:35]}...', Manifest: '{q_data['prompt'][:35]}...'"
                                    )
                                    conflicts.append(msg)
                                    stats['quizzes_existing'] += 1
                                    if overwrite_conflicts:
                                        alt_quiz.prompt = q_data['prompt']
                                        alt_quiz.option_a = q_data['option_a']
                                        alt_quiz.option_b = q_data['option_b']
                                        alt_quiz.option_c = q_data['option_c']
                                        alt_quiz.option_d = q_data['option_d']
                                        alt_quiz.correct_option = q_data['correct_option'].strip().upper()
                                        alt_quiz.explanation = q_data['explanation']
                                        alt_quiz.kids_hint = q_data.get('kids_hint', '')
                                        alt_quiz.save()
                                        self.stdout.write(self.style.NOTICE(f"  [OVERWRITTEN] Updated Quiz on '{cap_title}'."))
                                    else:
                                        self.stdout.write(self.style.WARNING(f"  [CONFLICT] {msg} (Preserved existing)"))
                                else:
                                    QuizQuestion.objects.create(
                                        capsule=capsule,
                                        prompt=q_data['prompt'],
                                        option_a=q_data['option_a'],
                                        option_b=q_data['option_b'],
                                        option_c=q_data['option_c'],
                                        option_d=q_data['option_d'],
                                        correct_option=q_data['correct_option'].strip().upper(),
                                        explanation=q_data['explanation'],
                                        kids_hint=q_data.get('kids_hint', ''),
                                    )
                                    stats['quizzes_created'] += 1
                            else:
                                stats['quizzes_existing'] += 1
                                q_diffs = []
                                for fld in ['option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'explanation']:
                                    expected = q_data[fld].strip().upper() if fld == 'correct_option' else q_data[fld]
                                    if getattr(quiz_q, fld) != expected:
                                        q_diffs.append(fld)
                                if (quiz_q.kids_hint or '') != (q_data.get('kids_hint') or ''):
                                    q_diffs.append('kids_hint')
                                if q_diffs:
                                    msg = f"Quiz on Capsule '{cap_title}': Existing question differs in {', '.join(q_diffs)}."
                                    conflicts.append(msg)
                                    if overwrite_conflicts:
                                        for fld in ['option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'explanation']:
                                            val = q_data[fld].strip().upper() if fld == 'correct_option' else q_data[fld]
                                            setattr(quiz_q, fld, val)
                                        quiz_q.kids_hint = q_data.get('kids_hint', '')
                                        quiz_q.save()
                                        self.stdout.write(self.style.NOTICE(f"  [OVERWRITTEN] Updated Quiz on '{cap_title}'."))
                                    else:
                                        self.stdout.write(self.style.WARNING(f"  [CONFLICT] {msg} (Preserved existing)"))

        return stats, conflicts

    def handle(self, *args, **options):
        check_only = options.get('check_only', False)
        overwrite_conflicts = options.get('overwrite_conflicts', False)
        fixture_rel = options.get('fixture')
        fixture_path = Path(fixture_rel)
        if not fixture_path.is_absolute():
            fixture_path = Path(settings.BASE_DIR) / fixture_rel

        if not fixture_path.exists():
            raise CommandError(f"Catalogue fixture not found at path: {fixture_path}")

        try:
            with open(fixture_path, 'r', encoding='utf-8') as f:
                courses_data = json.load(f)
        except Exception as e:
            raise CommandError(f"Failed to read or parse fixture JSON: {e}")

        # 1. Strict pre-validation of entire manifest
        self.validate_manifest(courses_data)
        self.stdout.write(self.style.SUCCESS(
            f"Validated manifest: {len(courses_data)} courses defined in {fixture_path.name}"
        ))

        # 2. Check-only inspection
        if check_only:
            self.stdout.write(self.style.NOTICE("DRY RUN (--check-only active). Inspecting active database..."))
            planned, existing, conflicts = self.inspect_catalogue(courses_data)

            self.stdout.write("Database Inspection Summary:")
            self.stdout.write(
                f"  Planned Creations:\n"
                f"    - Subjects: {planned['subjects']}\n"
                f"    - Topics:   {planned['topics']}\n"
                f"    - Capsules: {planned['capsules']}\n"
                f"    - Quizzes:  {planned['quizzes']}"
            )
            self.stdout.write(
                f"  Existing (Matching):\n"
                f"    - Subjects: {existing['subjects']}\n"
                f"    - Topics:   {existing['topics']}\n"
                f"    - Capsules: {existing['capsules']}\n"
                f"    - Quizzes:  {existing['quizzes']}"
            )
            if conflicts:
                self.stdout.write(self.style.WARNING(f"  Detected Conflicts ({len(conflicts)}):"))
                for c in conflicts:
                    self.stdout.write(self.style.WARNING(f"    - {c}"))
            else:
                self.stdout.write(self.style.SUCCESS("  Detected Conflicts: 0"))

            self.stdout.write(self.style.SUCCESS(
                "Dry-run validation successful. No database changes were made."
            ))
            return

        # 3. Atomic Database Import
        stats, conflicts = self.import_catalogue(courses_data, overwrite_conflicts=overwrite_conflicts)

        self.stdout.write(self.style.SUCCESS(
            f"Catalogue import completed successfully!\n"
            f"  - Subjects: {stats['subjects_created']} created, {stats['subjects_existing']} existing\n"
            f"  - Topics:   {stats['topics_created']} created, {stats['topics_existing']} existing\n"
            f"  - Capsules: {stats['capsules_created']} created, {stats['capsules_existing']} existing\n"
            f"  - Quizzes:  {stats['quizzes_created']} created, {stats['quizzes_existing']} existing"
        ))
        if conflicts:
            self.stdout.write(self.style.WARNING(f"Notice: {len(conflicts)} conflict(s) encountered during import."))

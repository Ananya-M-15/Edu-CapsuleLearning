from django.test import TestCase, Client
from django.contrib.auth import get_user_model, authenticate
from learning.models import (
    Subject, Topic, Capsule, UserProgress,
    LearnerProfile, QuizQuestion, UserQuizAttempt, ReviewSchedule
)
from django.urls import reverse
from django.utils import timezone
from learning.forms import SignUpForm
from educaps_project.settings import get_bool_env

User = get_user_model()


class UserSignupTests(TestCase):
    """Automated tests for user registration, input validation, and password security."""

    def test_successful_signup_creates_user_with_hashed_password(self):
        form_data = {
            'username': 'NewLearner',
            'password': 'StrongPassword2026!',
            'password2': 'StrongPassword2026!'
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Form errors: {form.errors}")
        user = form.save()

        # Verify user exists in database
        self.assertEqual(user.username, 'NewLearner')
        self.assertTrue(user.is_active)
        # Verify password is encrypted with PBKDF2 algorithm, never raw text
        self.assertTrue(user.password.startswith('pbkdf2_sha256$'))
        self.assertTrue(user.check_password('StrongPassword2026!'))
        self.assertFalse(user.check_password('WrongPassword!'))

    def test_signup_with_invalid_password_returns_validation_error_without_key_error(self):
        """
        Regression test: When password fails validation (e.g. too short),
        clean_password2 must not raise a KeyError: 'password'.
        """
        form_data = {
            'username': 'ShortPassUser',
            'password': '123',  # violates minimum length and numeric validators
            'password2': '123'
        }
        form = SignUpForm(data=form_data)
        # Form should be invalid, but must NOT raise KeyError: 'password'
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)

    def test_signup_with_mismatched_passwords_returns_error(self):
        form_data = {
            'username': 'MismatchUser',
            'password': 'ValidPassword2026!',
            'password2': 'DifferentPassword2026!'
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
        self.assertIn("Passwords don't match.", form.errors['password2'])

    def test_signup_strips_leading_and_trailing_whitespace(self):
        form_data = {
            'username': '  PaddedLearner  ',
            'password': 'ValidPassword2026!',
            'password2': 'ValidPassword2026!'
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Form errors: {form.errors}")
        user = form.save()
        self.assertEqual(user.username, 'PaddedLearner')

    def test_duplicate_username_rejected_case_insensitively(self):
        User.objects.create_user(username='ExistingUser', password='InitialPassword2026!')

        # Exact match
        form_exact = SignUpForm(data={
            'username': 'ExistingUser',
            'password': 'NewPassword2026!',
            'password2': 'NewPassword2026!'
        })
        self.assertFalse(form_exact.is_valid())
        self.assertIn('username', form_exact.errors)

        # Case-insensitive match (e.g. mobile lowercase signup)
        form_lower = SignUpForm(data={
            'username': 'existinguser',
            'password': 'NewPassword2026!',
            'password2': 'NewPassword2026!'
        })
        self.assertFalse(form_lower.is_valid())
        self.assertIn('username', form_lower.errors)

    def test_signup_view_post_redirects_and_authenticates(self):
        client = Client()
        response = client.post(reverse('signup'), {
            'username': 'WebSignupUser',
            'password': 'WebPassword2026!',
            'password2': 'WebPassword2026!'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.context['user'].username, 'WebSignupUser')


class UserAuthenticationTests(TestCase):
    """Automated tests for login, case-insensitivity, logout, and credential security."""

    def setUp(self):
        self.user = User.objects.create_user(
            username='EduLearner',
            password='TargetPassword2026!'
        )

    def test_login_with_exact_credentials_succeeds(self):
        client = Client()
        response = client.post(reverse('login'), {
            'username': 'EduLearner',
            'password': 'TargetPassword2026!'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.context['user'].username, 'EduLearner')

    def test_login_with_case_insensitive_username_succeeds(self):
        """
        Users registering with auto-capitalization on mobile keyboards
        can sign in with lowercase, uppercase, or mixed-case username.
        """
        client = Client()

        # Test lowercase
        response_lower = client.post(reverse('login'), {
            'username': 'edulearner',
            'password': 'TargetPassword2026!'
        }, follow=True)
        self.assertEqual(response_lower.status_code, 200)
        self.assertTrue(response_lower.context['user'].is_authenticated)

        client.logout()

        # Test uppercase
        response_upper = client.post(reverse('login'), {
            'username': 'EDULEARNER',
            'password': 'TargetPassword2026!'
        }, follow=True)
        self.assertEqual(response_upper.status_code, 200)
        self.assertTrue(response_upper.context['user'].is_authenticated)

    def test_login_with_whitespace_in_username_succeeds(self):
        client = Client()
        response = client.post(reverse('login'), {
            'username': '  EduLearner  ',
            'password': 'TargetPassword2026!'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_with_incorrect_password_shows_form_error(self):
        client = Client()
        response = client.post(reverse('login'), {
            'username': 'EduLearner',
            'password': 'WrongPassword123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertIn("Your username and password didn't match", response.content.decode('utf-8'))

    def test_login_with_non_existent_username_shows_form_error_without_500(self):
        client = Client()
        response = client.post(reverse('login'), {
            'username': 'GhostUserDoesNotExist',
            'password': 'AnyPassword123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertIn("Your username and password didn't match", response.content.decode('utf-8'))

    def test_inactive_user_cannot_login(self):
        """Inactive user accounts are rejected by authentication and login views."""
        User.objects.create_user(
            username='InactiveLearner',
            password='InactivePassword2026!',
            is_active=False
        )
        client = Client()
        response = client.post(reverse('login'), {
            'username': 'InactiveLearner',
            'password': 'InactivePassword2026!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertIn("Your username and password didn't match", response.content.decode('utf-8'))

    def test_login_session_creation_and_redirect_to_dashboard(self):
        """Successful login creates a valid session and redirects to dashboard."""
        client = Client()
        response = client.post(reverse('login'), {
            'username': 'EduLearner',
            'password': 'TargetPassword2026!'
        })
        # Verifies 302 redirect to dashboard
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('dashboard'))
        # Verifies session contains authenticated user ID
        self.assertEqual(int(client.session['_auth_user_id']), self.user.id)

    def test_login_respects_next_parameter_redirect(self):
        """Login view correctly redirects to the requested 'next' target URL."""
        client = Client()
        response = client.post(reverse('login') + '?next=' + reverse('reviews'), {
            'username': 'EduLearner',
            'password': 'TargetPassword2026!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('reviews'))

    def test_case_insensitive_duplicate_legacy_accounts_can_both_authenticate(self):
        """
        Regression test: In existing databases where multiple case-variant accounts
        coexist (e.g. 'Ananya' and 'ananya'), CaseInsensitiveModelBackend gracefully
        resolves and authenticates both accounts according to their valid passwords,
        rather than raising MultipleObjectsReturned and failing.
        """
        user_upper = User(username='LegacyCase')
        user_upper.set_password('UpperPass2026!')
        user_upper.save()

        user_lower = User(username='legacycase')
        user_lower.set_password('LowerPass2026!')
        user_lower.save()

        client = Client()

        # 1. User with password for user_upper signs in using upper-case username
        resp1 = client.post(reverse('login'), {
            'username': 'LegacyCase',
            'password': 'UpperPass2026!'
        }, follow=True)
        self.assertEqual(resp1.status_code, 200)
        self.assertTrue(resp1.context['user'].is_authenticated)
        self.assertEqual(resp1.context['user'].id, user_upper.id)
        client.logout()

        # 2. User with password for user_upper signs in using lower-case username
        resp2 = client.post(reverse('login'), {
            'username': 'legacycase',
            'password': 'UpperPass2026!'
        }, follow=True)
        self.assertEqual(resp2.status_code, 200)
        self.assertTrue(resp2.context['user'].is_authenticated)
        self.assertEqual(resp2.context['user'].id, user_upper.id)
        client.logout()

        # 3. User with password for user_lower signs in using lower-case username
        resp3 = client.post(reverse('login'), {
            'username': 'legacycase',
            'password': 'LowerPass2026!'
        }, follow=True)
        self.assertEqual(resp3.status_code, 200)
        self.assertTrue(resp3.context['user'].is_authenticated)
        self.assertEqual(resp3.context['user'].id, user_lower.id)
        client.logout()

        # 4. User with password for user_lower signs in using upper-case username
        resp4 = client.post(reverse('login'), {
            'username': 'LegacyCase',
            'password': 'LowerPass2026!'
        }, follow=True)
        self.assertEqual(resp4.status_code, 200)
        self.assertTrue(resp4.context['user'].is_authenticated)
        self.assertEqual(resp4.context['user'].id, user_lower.id)
        client.logout()

        # 5. User signs in with all-caps username
        resp5 = client.post(reverse('login'), {
            'username': 'LEGACYCASE',
            'password': 'UpperPass2026!'
        }, follow=True)
        self.assertEqual(resp5.status_code, 200)
        self.assertTrue(resp5.context['user'].is_authenticated)
        self.assertEqual(resp5.context['user'].id, user_upper.id)
        client.logout()

        # 6. Wrong password fails
        resp6 = client.post(reverse('login'), {
            'username': 'legacycase',
            'password': 'WrongPassword123!'
        })
        self.assertEqual(resp6.status_code, 200)
        self.assertFalse(resp6.context['user'].is_authenticated)

    def test_authentication_uses_default_database(self):
        """Verifies authentication operates on the configured default database."""
        from django.db import DEFAULT_DB_ALIAS
        self.assertEqual(User.objects.db, DEFAULT_DB_ALIAS)

    def test_logout_clears_session_and_redirects(self):
        client = Client()
        client.login(username='EduLearner', password='TargetPassword2026!')
        response = client.post(reverse('logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)


class UserProgressIsolationTests(TestCase):
    """Automated tests for capsule completion, idempotency, and user data isolation."""

    def setUp(self):
        self.user_a = User.objects.create_user(username='UserA', password='PasswordA2026!')
        self.user_b = User.objects.create_user(username='UserB', password='PasswordB2026!')

        self.subject = Subject.objects.create(name='Personal Finance', icon_class='fas fa-coins')
        self.topic = Topic.objects.create(subject=self.subject, title='Emergency Fund', order=1)
        self.capsule_1 = Capsule.objects.create(
            topic=self.topic,
            title='Day 1: What is an Emergency Fund?',
            front_content='What is an emergency fund?',
            back_content='Savings set aside for unexpected expenses.',
            order=1
        )
        self.capsule_2 = Capsule.objects.create(
            topic=self.topic,
            title='Day 2: How much to save?',
            front_content='How many months of expenses?',
            back_content='3 to 6 months of living expenses.',
            order=2
        )

        # User A subscribes to the subject
        self.user_a.subscribed_subjects.add(self.subject)

    def test_completing_capsule_records_progress_for_authenticated_user(self):
        client = Client()
        client.login(username='UserA', password='PasswordA2026!')

        response = client.post(reverse('complete_capsule', args=[self.capsule_1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'success', 'message': 'Progress saved!'})

        # Verify progress recorded in database
        self.assertTrue(UserProgress.objects.filter(user=self.user_a, capsule=self.capsule_1).exists())

    def test_repeated_completion_is_idempotent_and_creates_no_duplicates(self):
        client = Client()
        client.login(username='UserA', password='PasswordA2026!')

        # Send completion twice
        client.post(reverse('complete_capsule', args=[self.capsule_1.id]))
        client.post(reverse('complete_capsule', args=[self.capsule_1.id]))

        # Count must remain exactly 1
        count = UserProgress.objects.filter(user=self.user_a, capsule=self.capsule_1).count()
        self.assertEqual(count, 1)

    def test_progress_is_strictly_isolated_between_users(self):
        # User A completes capsule 1
        UserProgress.objects.create(user=self.user_a, capsule=self.capsule_1)

        # User B has completed 0 capsules
        self.assertEqual(UserProgress.objects.filter(user=self.user_b).count(), 0)
        self.assertTrue(UserProgress.objects.filter(user=self.user_a, capsule=self.capsule_1).exists())
        self.assertFalse(UserProgress.objects.filter(user=self.user_b, capsule=self.capsule_1).exists())

    def test_unauthenticated_completion_redirects_to_login(self):
        client = Client()
        response = client.post(reverse('complete_capsule', args=[self.capsule_1.id]))
        # @login_required redirects unauthenticated requests
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_dashboard_reflects_accurate_progress_calculations(self):
        client = Client()
        client.login(username='UserA', password='PasswordA2026!')

        # Initial: 0 completed out of 2
        response = client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['completed_count'], 0)
        self.assertEqual(response.context['total_capsules'], 2)
        self.assertEqual(response.context['progress_percentage'], 0)

        # Complete 1 capsule: 1 completed out of 2 (50%)
        UserProgress.objects.create(user=self.user_a, capsule=self.capsule_1)
        response2 = client.get(reverse('dashboard'))
        self.assertEqual(response2.context['completed_count'], 1)
        self.assertEqual(response2.context['total_capsules'], 2)
        self.assertEqual(response2.context['progress_percentage'], 50)


class SubjectSubscriptionTests(TestCase):
    """Automated tests for subject subscriptions and safe error handling."""

    def setUp(self):
        self.user = User.objects.create_user(username='SubLearner', password='Password2026!')
        self.subject = Subject.objects.create(name='Psychology', icon_class='fas fa-brain')

    def test_toggle_subscription_adds_and_removes_subject(self):
        client = Client()
        client.login(username='SubLearner', password='Password2026!')

        # Toggle: Add subscription
        response = client.post(reverse('toggle_subscription', args=[self.subject.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.subject, self.user.subscribed_subjects.all())

        # Toggle: Remove subscription
        response2 = client.post(reverse('toggle_subscription', args=[self.subject.id]), follow=True)
        self.assertEqual(response2.status_code, 200)
        self.assertNotIn(self.subject, self.user.subscribed_subjects.all())

    def test_completing_non_existent_capsule_returns_404(self):
        client = Client()
        client.login(username='SubLearner', password='Password2026!')
        response = client.post(reverse('complete_capsule', args=[999999]))
        self.assertEqual(response.status_code, 404)

    def test_subscribing_to_non_existent_subject_returns_404(self):
        client = Client()
        client.login(username='SubLearner', password='Password2026!')
        response = client.post(reverse('toggle_subscription', args=[999999]))
        self.assertEqual(response.status_code, 404)


class SecurityAndSettingsTests(TestCase):
    """Automated tests for configuration utilities and environment security."""

    def test_get_bool_env_truthy_and_falsy_parsing(self):
        import os
        for truthy in ['true', 'True', 'TRUE', '1', 'yes', 'YES', 't', 'y']:
            os.environ['TEST_BOOL'] = truthy
            self.assertTrue(get_bool_env('TEST_BOOL'))

        for falsy in ['false', 'False', 'FALSE', '0', 'no', 'NO', 'f', 'random', '']:
            os.environ['TEST_BOOL'] = falsy
            self.assertFalse(get_bool_env('TEST_BOOL'))

    def test_case_insensitive_backend_timing_mitigation_on_missing_user(self):
        from learning.backends import CaseInsensitiveModelBackend
        backend = CaseInsensitiveModelBackend()
        # Non-existent user should cleanly return None without crashing
        result = backend.authenticate(None, username='DoesNotExistUser', password='SomePassword!')
        self.assertIsNone(result)

        # Empty credentials should return None
        self.assertIsNone(backend.authenticate(None, username='', password=''))
        self.assertIsNone(backend.authenticate(None, username='User', password=''))


class LearnerProfileTests(TestCase):
    """Automated tests for LearnerProfile creation, persistent modes, and mentor properties."""

    def test_user_creation_automatically_creates_learner_profile(self):
        user = User.objects.create_user(username='ModeLearner', password='Password2026!')
        self.assertTrue(hasattr(user, 'profile'))
        self.assertEqual(user.profile.learner_mode, 'standard')
        self.assertEqual(user.profile.mentor_name, 'Anaya')
        self.assertIn('anaya.jpg', user.profile.mentor_image)

    def test_kids_mode_mentor_properties(self):
        user = User.objects.create_user(username='KidLearner', password='Password2026!')
        user.profile.learner_mode = 'kids'
        user.profile.save()
        self.assertTrue(user.profile.is_kids_mode)
        self.assertEqual(user.profile.mentor_name, 'Cappy')
        self.assertIn('cappy.jpg', user.profile.mentor_image)
        self.assertIn('Cappy', user.profile.mentor_greeting)

    def test_legacy_user_without_profile_handled_safely(self):
        user = User.objects.create_user(username='LegacyUser', password='Password2026!')
        # Delete profile to simulate pre-migration legacy user
        user.profile.delete()
        user.refresh_from_db()
        self.assertFalse(hasattr(user, 'profile'))

        from learning.services import get_or_create_learner_profile
        profile = get_or_create_learner_profile(user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.learner_mode, 'standard')


class QuizAndAssessmentTests(TestCase):
    """Automated tests for QuizQuestion, UserQuizAttempt, and topic weakness detection."""

    def setUp(self):
        self.user = User.objects.create_user(username='QuizUser', password='Password2026!')
        self.subject = Subject.objects.create(name='Investing 101')
        self.topic = Topic.objects.create(subject=self.subject, title='Compound Interest', order=1)
        self.capsule = Capsule.objects.create(
            topic=self.topic,
            title='The Power of Compounding',
            front_content='What is compound interest?',
            back_content='Interest earned on interest and principal.',
            order=1
        )
        self.question = QuizQuestion.objects.create(
            capsule=self.capsule,
            prompt='What does compound interest earn interest on?',
            option_a='Only the original principal',
            option_b='Both the principal and previously earned interest',
            option_c='Only government bonds',
            option_d='Bank service fees',
            correct_option='B',
            explanation='Compound interest applies to the initial principal plus accumulated interest from previous periods.',
            kids_hint='Think about money making more money on top of money!'
        )

    def test_quiz_question_correctness_verification(self):
        self.assertTrue(self.question.is_correct('B'))
        self.assertTrue(self.question.is_correct('b'))
        self.assertFalse(self.question.is_correct('A'))
        self.assertFalse(self.question.is_correct('C'))
        self.assertFalse(self.question.is_correct(''))

    def test_quiz_attempt_recording_and_weakness_detection(self):
        from learning.services import calculate_topic_weaknesses

        # Record an incorrect attempt
        UserQuizAttempt.objects.create(
            user=self.user,
            question=self.question,
            selected_option='A',
            is_correct=False
        )

        weaknesses = calculate_topic_weaknesses(self.user)
        self.assertEqual(len(weaknesses), 1)
        self.assertEqual(weaknesses[0]['topic'], self.topic)
        self.assertEqual(weaknesses[0]['accuracy'], 0)
        self.assertTrue(weaknesses[0]['needs_review'])

        # Now record 3 correct attempts
        for _ in range(3):
            UserQuizAttempt.objects.create(
                user=self.user,
                question=self.question,
                selected_option='B',
                is_correct=True
            )

        updated_weaknesses = calculate_topic_weaknesses(self.user)
        # 3 out of 4 correct = 75% accuracy -> no longer needs urgent review
        self.assertEqual(updated_weaknesses[0]['accuracy'], 75)
        self.assertFalse(updated_weaknesses[0]['needs_review'])


class SpacedRepetitionSM2Tests(TestCase):
    """Automated tests for SuperMemo SM-2 algorithm mathematical edge cases."""

    def setUp(self):
        self.user = User.objects.create_user(username='SM2User', password='Password2026!')
        self.subject = Subject.objects.create(name='Cognitive Science')
        self.topic = Topic.objects.create(subject=self.subject, title='Memory Retention', order=1)
        self.capsule = Capsule.objects.create(
            topic=self.topic,
            title='Ebbinghaus Forgetting Curve',
            front_content='How quickly do we forget information?',
            back_content='Over 50% is forgotten within 1 hour unless reinforced.',
            order=1
        )
        self.schedule = ReviewSchedule.objects.create(
            user=self.user,
            capsule=self.capsule
        )

    def test_initial_successful_review_sets_one_day_interval(self):
        # Grade 5 (perfect recall)
        self.schedule.record_review(grade=5)
        self.assertEqual(self.schedule.repetition_number, 1)
        self.assertEqual(self.schedule.interval_days, 1)
        # EF increased from 2.5: 2.5 + (0.1 - 0) = 2.6
        self.assertEqual(self.schedule.easiness_factor, 2.6)

    def test_second_successful_review_sets_six_day_interval(self):
        self.schedule.record_review(grade=5)
        self.schedule.record_review(grade=5)
        self.assertEqual(self.schedule.repetition_number, 2)
        self.assertEqual(self.schedule.interval_days, 6)

    def test_third_review_scales_interval_by_easiness_factor(self):
        self.schedule.record_review(grade=5)
        self.schedule.record_review(grade=5)
        # rep=2, interval=6, EF=2.7
        self.schedule.record_review(grade=4)
        # Grade 4: EF' = 2.7 + (0.1 - 1 * (0.08 + 0.02)) = 2.7 + 0 = 2.7
        # Interval = ceil(6 * 2.7) = 17 days
        self.assertEqual(self.schedule.repetition_number, 3)
        self.assertEqual(self.schedule.interval_days, 17)

    def test_failed_review_resets_repetition_and_interval(self):
        # Advance through 2 reviews
        self.schedule.record_review(grade=5)
        self.schedule.record_review(grade=5)
        self.assertEqual(self.schedule.repetition_number, 2)

        # Failed recall (grade = 2)
        self.schedule.record_review(grade=2)
        self.assertEqual(self.schedule.repetition_number, 0)
        self.assertEqual(self.schedule.interval_days, 1)

    def test_easiness_factor_never_drops_below_minimum_boundary_1_3(self):
        # Repeated severe blackouts (grade 0)
        for _ in range(10):
            self.schedule.record_review(grade=0)
        self.assertGreaterEqual(self.schedule.easiness_factor, 1.3)
        self.assertEqual(self.schedule.easiness_factor, 1.3)


class AITutorServiceTests(TestCase):
    """Automated tests for Cappy & Anaya AI Tutor service logic and fallbacks."""

    def setUp(self):
        self.user = User.objects.create_user(username='TutorLearner', password='Password2026!')
        self.subject = Subject.objects.create(name='Logic')
        self.topic = Topic.objects.create(subject=self.subject, title='Inductive Reasoning', order=1)
        self.capsule = Capsule.objects.create(
            topic=self.topic,
            title='Patterns to Rules',
            front_content='Inductive reasoning moves from specific observations to broad generalizations.',
            back_content='It provides probabilistic support, not absolute certainty.',
            order=1
        )
        self.question = QuizQuestion.objects.create(
            capsule=self.capsule,
            prompt='What level of certainty does inductive reasoning give?',
            option_a='Absolute mathematical certainty',
            option_b='Probabilistic support',
            option_c='Zero confidence',
            option_d='Guaranteed proof',
            correct_option='B',
            explanation='Inductive logic yields conclusions that are probable, not deductive certainties.',
            kids_hint='Think about looking at 10 white swans - you think the next one is white, but could it be black?'
        )

    def test_cappy_mentor_explanation_for_kids_mode(self):
        from learning.ai_tutor import explain_capsule
        explanation = explain_capsule(self.capsule, mode='kids')
        self.assertEqual(explanation['mentor'], 'Cappy')
        self.assertIn('Cappy', explanation['cappy_cheer'])
        self.assertIn('Inductive reasoning', explanation['core_concept'])

    def test_anaya_mentor_explanation_for_standard_mode(self):
        from learning.ai_tutor import explain_capsule
        explanation = explain_capsule(self.capsule, mode='standard')
        self.assertEqual(explanation['mentor'], 'Anaya')
        self.assertIn('Anaya', explanation['anaya_guidance'])
        self.assertIn('Key Competency', explanation['takeaway'])

    def test_progressive_hints_respect_mode(self):
        from learning.ai_tutor import generate_quiz_hint
        kids_hint = generate_quiz_hint(self.question, mode='kids')
        standard_hint = generate_quiz_hint(self.question, mode='standard')

        self.assertIn('Cappy', kids_hint)
        self.assertIn('white swans', kids_hint)

        self.assertIn('Anaya', standard_hint)
        self.assertIn('reverse card', standard_hint)

    def test_query_answering_stays_grounded_and_handles_out_of_scope(self):
        from learning.ai_tutor import answer_capsule_query

        # In-scope query
        ans_kids = answer_capsule_query(self.capsule, 'What is inductive reasoning?', mode='kids')
        self.assertEqual(ans_kids['mentor'], 'Cappy')
        self.assertIn('probabilistic', ans_kids['response'].lower())

        # Out-of-scope query
        ans_out = answer_capsule_query(self.capsule, 'How do rockets fly to Mars?', mode='standard')
        self.assertEqual(ans_out['mentor'], 'Anaya')
        self.assertIn('reaches beyond the scope', ans_out['response'])


class SprintEndToEndIntegrationTests(TestCase):
    """End-to-end integration tests for public landing, mode switching, quizzes, reviews, and PWA."""

    def setUp(self):
        self.user = User.objects.create_user(username='SprintLearner', password='Password2026!')
        self.subject = Subject.objects.create(name='Decision Making', icon_class='fas fa-balance-scale')
        self.topic = Topic.objects.create(subject=self.subject, title='Cognitive Biases', order=1)
        self.capsule = Capsule.objects.create(
            topic=self.topic,
            title='Confirmation Bias',
            front_content='What is confirmation bias?',
            back_content='The tendency to search for, interpret, and recall information that confirms preexisting beliefs.',
            order=1
        )
        self.question = QuizQuestion.objects.create(
            capsule=self.capsule,
            prompt='How does confirmation bias affect decision making?',
            option_a='It causes people to overlook disconfirming evidence.',
            option_b='It guarantees 100% objective logical analysis.',
            option_c='It only affects computer algorithms.',
            option_d='It eliminates emotional reasoning.',
            correct_option='A',
            explanation='Confirmation bias leads individuals to systematically favor evidence confirming hypotheses while ignoring disconfirming data.',
            kids_hint='Think about only listening to people who agree with you!'
        )
        self.user.subscribed_subjects.add(self.subject)

    def test_public_homepage_renders_hero_and_mentors_for_anonymous_visitor(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Big Ideas. Small Capsules.', response.content.decode('utf-8'))
        self.assertIn('Cappy', response.content.decode('utf-8'))
        self.assertIn('Anaya', response.content.decode('utf-8'))

    def test_authenticated_user_visiting_home_has_access_with_dashboard_cta(self):
        """
        Phase 2: Authenticated user opens '/' -> public homepage remains available,
        with an obvious route back to their dashboard.
        """
        client = Client()
        client.login(username='SprintLearner', password='Password2026!')
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(reverse('dashboard'), response.content.decode('utf-8'))
        self.assertIn('Dashboard', response.content.decode('utf-8'))

    def test_course_search_returns_matching_subjects_and_topics(self):
        client = Client()
        # Search by subject name
        response = client.get(reverse('search') + '?q=Decision')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('Decision Making', content)

        # Search by topic title
        response_topic = client.get(reverse('search') + '?q=Cognitive')
        self.assertEqual(response_topic.status_code, 200)
        content_topic = response_topic.content.decode('utf-8')
        self.assertIn('Cognitive Biases', content_topic)

    def test_course_search_empty_query_redirects_to_library(self):
        client = Client()
        response = client.get(reverse('search') + '?q=   ')
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('library'), response.url)

    def test_course_search_non_matching_query_shows_empty_state(self):
        client = Client()
        response = client.get(reverse('search') + '?q=NonExistentKeywordXYZ')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn("couldn't find any courses matching your search", content)
        self.assertIn("No results found matching", content)

    def test_public_access_to_course_library(self):
        client = Client()
        response = client.get(reverse('library'))
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('Decision Making', content)
        self.assertIn('Cognitive Biases', content)

    def test_protected_routes_redirect_anonymous_users(self):
        client = Client()
        protected_routes = ['dashboard', 'learn', 'reviews', 'my_learning']
        for route_name in protected_routes:
            response = client.get(reverse(route_name))
            self.assertEqual(response.status_code, 302, f"Route {route_name} should redirect anonymous users")
            self.assertIn('/login/', response.url)

    def test_mode_selection_and_persistence(self):
        client = Client()
        client.login(username='SprintLearner', password='Password2026!')

        # GET mode selection
        get_resp = client.get(reverse('select_mode'))
        self.assertEqual(get_resp.status_code, 200)
        content = get_resp.content.decode('utf-8')
        # Mentor avatars match approved homepage hero artwork asset
        self.assertIn('images/hero-mentors.png', content)
        self.assertIn('class="mode-choice-img anaya-avatar-img"', content)
        self.assertIn('class="mode-choice-img cappy-avatar-img"', content)
        self.assertNotIn('class="mode-choice-img" src="/static/images/mentors/', content)

        # POST choose Kids Mode
        post_resp = client.post(reverse('select_mode'), {'mode': 'kids'}, follow=True)
        self.assertEqual(post_resp.status_code, 200)

        self.user.refresh_from_db()
        self.assertEqual(self.user.profile.learner_mode, 'kids')
        self.assertTrue(self.user.profile.mode_chosen)

    def test_mode_toggle_endpoint_switches_between_modes(self):
        client = Client()
        client.login(username='SprintLearner', password='Password2026!')

        # Initially standard
        self.assertEqual(self.user.profile.learner_mode, 'standard')

        # Toggle to kids
        toggle_resp = client.post(reverse('toggle_mode'), follow=True)
        self.assertEqual(toggle_resp.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.profile.learner_mode, 'kids')

        # Toggle back to standard
        toggle_resp2 = client.post(reverse('toggle_mode'), follow=True)
        self.assertEqual(toggle_resp2.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.profile.learner_mode, 'standard')

    def test_dashboard_renders_course_discovery_and_mentor_briefing(self):
        client = Client()
        client.login(username='SprintLearner', password='Password2026!')

        response = client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Anaya', response.content.decode('utf-8'))
        self.assertIn('Confirmation Bias', response.content.decode('utf-8'))

    def test_learn_view_renders_capsule_and_mentor_explanation(self):
        client = Client()
        client.login(username='SprintLearner', password='Password2026!')

        response = client.get(reverse('learn') + f'?capsule_id={self.capsule.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Confirmation Bias', response.content.decode('utf-8'))
        self.assertIn('Active Recall Check', response.content.decode('utf-8'))

    def test_submit_quiz_view_records_attempt_and_schedules_spaced_review(self):
        client = Client()
        client.login(username='SprintLearner', password='Password2026!')

        # Submit correct option
        response = client.post(reverse('submit_quiz', args=[self.question.id]), {
            'selected_option': 'A'
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertTrue(data['is_correct'])
        self.assertEqual(data['correct_option'], 'A')
        self.assertGreaterEqual(data['next_review_days'], 1)

        # Verify attempt record
        self.assertTrue(UserQuizAttempt.objects.filter(user=self.user, question=self.question, is_correct=True).exists())

        # Verify SM-2 ReviewSchedule record
        self.assertTrue(ReviewSchedule.objects.filter(user=self.user, capsule=self.capsule).exists())

    def test_tutor_ask_endpoint_returns_grounded_answer(self):
        client = Client()
        client.login(username='SprintLearner', password='Password2026!')

        response = client.post(reverse('tutor_ask', args=[self.capsule.id]), {
            'query': 'What is confirmation bias?'
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['mentor'], 'Anaya')
        self.assertIn('preexisting beliefs', data['response'].lower())

    def test_reviews_view_renders_spaced_repetition_queue(self):
        client = Client()
        client.login(username='SprintLearner', password='Password2026!')

        # Create a due review
        ReviewSchedule.objects.create(
            user=self.user,
            capsule=self.capsule,
            next_review_date=timezone.now().date()
        )

        response = client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Due for Review Today', response.content.decode('utf-8'))
        self.assertIn('Confirmation Bias', response.content.decode('utf-8'))

    def test_pwa_manifest_and_service_worker_endpoints(self):
        client = Client()

        # Manifest
        manifest_resp = client.get(reverse('manifest'))
        self.assertEqual(manifest_resp.status_code, 200)
        self.assertEqual(manifest_resp['Content-Type'], 'application/manifest+json')
        manifest_json = manifest_resp.json()
        self.assertEqual(manifest_json['short_name'], 'EduCaps')
        self.assertEqual(manifest_json['display'], 'standalone')

        # Service Worker
        sw_resp = client.get(reverse('service_worker'))
        self.assertEqual(sw_resp.status_code, 200)
        self.assertEqual(sw_resp['Content-Type'], 'application/javascript')
        self.assertIn('caches.open', sw_resp.content.decode('utf-8'))


class EnrolledCoursesAndReviewNoticeTests(TestCase):
    """
    Tests for /my-learning/ enrolled-courses filtering, empty state,
    cross-user enrollment isolation, toggle subscription, and review notice removal.
    """

    def setUp(self):
        self.user_a = User.objects.create_user(username='LearnerA', password='PasswordA2026!')
        self.user_b = User.objects.create_user(username='LearnerB', password='PasswordB2026!')

        self.subject1 = Subject.objects.create(name='Python Programming', description='Core Python skills.')
        self.subject2 = Subject.objects.create(name='Web Development', description='Full-stack web skills.')
        self.subject3 = Subject.objects.create(name='Machine Learning', description='AI fundamentals.')

        self.topic1 = Topic.objects.create(subject=self.subject1, title='Basics', order=1)
        self.capsule1 = Capsule.objects.create(
            topic=self.topic1,
            title='Python Variables',
            front_content='Front text',
            back_content='Back text',
            order=1
        )

    def test_user_enrolled_in_two_courses_sees_exactly_those_two_courses(self):
        """A user enrolled in two courses sees exactly those two courses, not unenrolled ones."""
        self.user_a.subscribed_subjects.add(self.subject1, self.subject2)

        client = Client()
        client.login(username='LearnerA', password='PasswordA2026!')

        response = client.get(reverse('my_learning'))
        self.assertEqual(response.status_code, 200)

        # Context contains exactly the two enrolled courses
        enrolled_in_context = list(response.context['enrolled_subjects'])
        self.assertEqual(len(enrolled_in_context), 2)
        self.assertIn(self.subject1, enrolled_in_context)
        self.assertIn(self.subject2, enrolled_in_context)
        self.assertNotIn(self.subject3, enrolled_in_context)

        # Content verification
        content = response.content.decode('utf-8')
        self.assertIn('Python Programming', content)
        self.assertIn('Web Development', content)
        self.assertNotIn('Machine Learning', content)

        # "Enrolled" badge appears, but "Available" badge does NOT appear
        self.assertIn('status-enrolled-yes', content)
        self.assertNotIn('status-enrolled-no', content)
        self.assertNotIn('>Available<', content)

    def test_unenrolled_courses_do_not_appear_on_page(self):
        """Unenrolled courses never appear on /my-learning/."""
        self.user_a.subscribed_subjects.add(self.subject1)

        client = Client()
        client.login(username='LearnerA', password='PasswordA2026!')

        response = client.get(reverse('my_learning'))
        content = response.content.decode('utf-8')

        self.assertIn('Python Programming', content)
        self.assertNotIn('Web Development', content)
        self.assertNotIn('Machine Learning', content)

    def test_user_with_no_enrollments_sees_empty_state_and_library_link(self):
        """A user with no enrollments sees clean empty state with a link to course library."""
        client = Client()
        client.login(username='LearnerA', password='PasswordA2026!')

        response = client.get(reverse('my_learning'))
        self.assertEqual(response.status_code, 200)

        content = response.content.decode('utf-8')
        self.assertIn("You haven't enrolled in any courses yet", content)
        self.assertIn(reverse('library'), content)
        self.assertIn('Explore Course Library', content)

        # None of the courses should appear
        self.assertNotIn('Python Programming', content)
        self.assertNotIn('Web Development', content)
        self.assertNotIn('Machine Learning', content)

    def test_different_users_cannot_see_each_others_enrollments(self):
        """User A sees only User A's enrollments; User B sees only User B's enrollments."""
        self.user_a.subscribed_subjects.add(self.subject1)
        self.user_b.subscribed_subjects.add(self.subject2)

        client_a = Client()
        client_a.login(username='LearnerA', password='PasswordA2026!')
        resp_a = client_a.get(reverse('my_learning'))
        content_a = resp_a.content.decode('utf-8')
        self.assertIn('Python Programming', content_a)
        self.assertNotIn('Web Development', content_a)

        client_b = Client()
        client_b.login(username='LearnerB', password='PasswordB2026!')
        resp_b = client_b.get(reverse('my_learning'))
        content_b = resp_b.content.decode('utf-8')
        self.assertIn('Web Development', content_b)
        self.assertNotIn('Python Programming', content_b)

    def test_review_notice_absent_from_my_learning_and_dashboard(self):
        """The 'Due for Spaced Review' notice is absent from /my-learning/ and /dashboard/."""
        self.user_a.subscribed_subjects.add(self.subject1)
        # Create a due review
        ReviewSchedule.objects.create(
            user=self.user_a,
            capsule=self.capsule1,
            next_review_date=timezone.now().date(),
            interval_days=1,
            repetition_number=1
        )

        client = Client()
        client.login(username='LearnerA', password='PasswordA2026!')

        # Verify /my-learning/
        resp_my_learning = client.get(reverse('my_learning'))
        self.assertEqual(resp_my_learning.status_code, 200)
        self.assertNotIn('Due for Spaced Review', resp_my_learning.content.decode('utf-8'))
        self.assertNotIn('badge-review-alert', resp_my_learning.content.decode('utf-8'))

        # Verify /dashboard/
        resp_dashboard = client.get(reverse('dashboard'))
        self.assertEqual(resp_dashboard.status_code, 200)
        self.assertNotIn('Due for Spaced Review', resp_dashboard.content.decode('utf-8'))
        self.assertNotIn('badge-review-alert', resp_dashboard.content.decode('utf-8'))

    def test_reviews_page_and_spaced_repetition_remain_operational(self):
        """The /reviews/ route and spaced-repetition functionality remain fully operational."""
        self.user_a.subscribed_subjects.add(self.subject1)
        ReviewSchedule.objects.create(
            user=self.user_a,
            capsule=self.capsule1,
            next_review_date=timezone.now().date(),
            interval_days=1,
            repetition_number=1
        )

        client = Client()
        client.login(username='LearnerA', password='PasswordA2026!')

        response = client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('Spaced Repetition', content)
        self.assertIn('Due for Review Today', content)
        self.assertIn('Python Variables', content)

    def test_toggle_subscription_enrolls_and_unenrolls(self):
        """Enrollment and unenrollment toggling works smoothly."""
        client = Client()
        client.login(username='LearnerA', password='PasswordA2026!')

        # Enroll
        resp = client.post(reverse('toggle_subscription', args=[self.subject1.id]))
        self.assertEqual(resp.status_code, 302)
        self.assertIn(self.user_a, self.subject1.subscribers.all())

        # Unenroll
        resp2 = client.post(reverse('toggle_subscription', args=[self.subject1.id]))
        self.assertEqual(resp2.status_code, 302)
        self.assertNotIn(self.user_a, self.subject1.subscribers.all())


class HomepageCleanupTests(TestCase):
    """
    Tests ensuring the homepage cleanup safely removes the tactile demo section
    and bottom registration CTA while preserving all other core homepage sections,
    auth routes, navigation, and learning flip cards.
    """

    def setUp(self):
        self.subject = Subject.objects.create(name='Personal Finance Mastery', description='Finance skills.')
        self.topic = Topic.objects.create(subject=self.subject, title='Emergency Funds', order=1)
        self.capsule = Capsule.objects.create(
            topic=self.topic,
            title='Building Cash Reserves',
            front_content='Front card lesson',
            back_content='Back card explanation',
            order=1
        )
        self.user = User.objects.create_user(username='TestLearner', password='TestPassword2026!')

    def test_homepage_renders_hero_and_core_content(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')

        # Hero section preserved
        self.assertIn('Big Ideas.', content)
        self.assertIn('Brighter You.', content)

        # Core sections preserved
        self.assertIn('What is EduCaps?', content)
        self.assertIn('How It Works', content)
        self.assertIn('Why EduCaps?', content)
        self.assertIn('Two Distinct Learning Modes', content)
        self.assertIn('Cappy the Robot', content)
        self.assertIn('Anaya', content)

    def test_foundational_courses_and_stats_strip_are_removed_from_homepage(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')

        # 1. Removed "Explore Foundational Courses" section
        self.assertNotIn('CURATED COURSES', content)
        self.assertNotIn('Explore Foundational Courses', content)
        self.assertNotIn('course-catalog-section', content)
        self.assertNotIn('Personal Finance Mastery', content)

        # 2. Removed homepage statistics strip
        self.assertNotIn('hero-stats-band', content)
        self.assertNotIn('50+ Micro-Capsules', content)
        self.assertNotIn('5 Foundational Courses', content)
        self.assertNotIn('2 Mentorship Modes', content)
        self.assertNotIn('SM-2 Spaced Repetition', content)

    def test_courses_catalogue_preserved_in_course_library(self):
        client = Client()
        response = client.get(reverse('library'))
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')

        # Course is displayed in the dedicated library
        self.assertIn('Personal Finance Mastery', content)
        self.assertIn('Finance skills.', content)

    def test_tactile_micro_learning_demo_section_is_removed(self):
        client = Client()
        response = client.get(reverse('home'))
        content = response.content.decode('utf-8')

        # Removed demo section strings
        self.assertNotIn('Tactile Micro-Learning', content)
        self.assertNotIn('How Capsule Learning Feels', content)
        self.assertNotIn('Click the flip card below to experience the active recall format.', content)
        self.assertNotIn('homeDemoCard', content)
        self.assertNotIn('What is an Emergency Fund?', content)
        self.assertNotIn('Tap to flip', content)
        self.assertNotIn('capsule-experience-showcase', content)

    def test_bottom_registration_cta_is_removed(self):
        client = Client()
        response = client.get(reverse('home'))
        content = response.content.decode('utf-8')

        # Removed bottom CTA strings
        self.assertNotIn('Ready to Build a Daily Learning Habit?', content)
        self.assertNotIn('Join EduCaps today and master essential real-world skills one 5-minute capsule at a time.', content)
        self.assertNotIn('final-banner-section', content)
        self.assertNotIn('final-cta-card', content)

    def test_auth_routes_and_navigation_links_remain_fully_accessible(self):
        client = Client()

        # Signup page accessible
        signup_resp = client.get(reverse('signup'))
        self.assertEqual(signup_resp.status_code, 200)

        # Login page accessible
        login_resp = client.get(reverse('login'))
        self.assertEqual(login_resp.status_code, 200)

        # Homepage navbar contains working links to signup and login
        home_resp = client.get(reverse('home'))
        home_content = home_resp.content.decode('utf-8')
        self.assertIn(reverse('signup'), home_content)
        self.assertIn(reverse('login'), home_content)

    def test_actual_lesson_flip_card_on_learn_page_preserved(self):
        self.user.subscribed_subjects.add(self.subject)
        client = Client()
        client.login(username='TestLearner', password='TestPassword2026!')
        response = client.get(reverse('learn') + f'?capsule_id={self.capsule.id}')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')

        # Lesson flip card structure intact
        self.assertIn('flip-card', content)
        self.assertIn('flip-card-inner', content)
        self.assertIn('flip-card-front', content)
        self.assertIn('flip-card-back', content)
        self.assertIn('Building Cash Reserves', content)


class CatalogueImportAndPwaTests(TestCase):
    """Automated tests for expanded catalogue import and PWA functionality."""

    def test_import_catalogue_check_only(self):
        from django.core.management import call_command
        from io import StringIO
        sub_before = Subject.objects.count()
        topic_before = Topic.objects.count()
        cap_before = Capsule.objects.count()
        quiz_before = QuizQuestion.objects.count()

        out = StringIO()
        call_command('import_catalogue', check_only=True, stdout=out)
        output = out.getvalue()
        self.assertIn('Dry-run validation successful', output)
        self.assertIn('Planned Creations:', output)
        self.assertIn('Existing (Matching):', output)
        self.assertIn('No database changes were made', output)

        # Confirm read-only: no changes made to database
        self.assertEqual(Subject.objects.count(), sub_before)
        self.assertEqual(Topic.objects.count(), topic_before)
        self.assertEqual(Capsule.objects.count(), cap_before)
        self.assertEqual(QuizQuestion.objects.count(), quiz_before)

    def test_import_catalogue_is_idempotent(self):
        from django.core.management import call_command
        from io import StringIO
        out1 = StringIO()
        call_command('import_catalogue', stdout=out1)
        sub_count1 = Subject.objects.count()
        topic_count1 = Topic.objects.count()
        cap_count1 = Capsule.objects.count()
        quiz_count1 = QuizQuestion.objects.count()

        # Run second time
        out2 = StringIO()
        call_command('import_catalogue', stdout=out2)
        sub_count2 = Subject.objects.count()
        topic_count2 = Topic.objects.count()
        cap_count2 = Capsule.objects.count()
        quiz_count2 = QuizQuestion.objects.count()

        self.assertEqual(sub_count1, sub_count2)
        self.assertEqual(topic_count1, topic_count2)
        self.assertEqual(cap_count1, cap_count2)
        self.assertEqual(quiz_count1, quiz_count2)
        self.assertIn('0 created', out2.getvalue())

    def test_existing_capsule_conflict_preserved_by_default(self):
        import tempfile
        import json
        from pathlib import Path
        from django.core.management import call_command
        from io import StringIO

        subject = Subject.objects.create(name="Conflict Course", description="Original Desc", icon_class="fas fa-book")
        topic = Topic.objects.create(subject=subject, title="Conflict Topic", order=0)
        capsule = Capsule.objects.create(
            topic=topic,
            title="Conflict Capsule",
            front_content="Original DB Front Content",
            back_content="Original DB Back Content",
            order=0
        )

        conflict_manifest = [{
            "name": "Conflict Course",
            "description": "Original Desc",
            "icon_class": "fas fa-book",
            "topics": [{
                "title": "Conflict Topic",
                "order": 0,
                "capsules": [{
                    "title": "Conflict Capsule",
                    "front_content": "Conflicting Front Content from Manifest",
                    "back_content": "Conflicting Back Content from Manifest",
                    "order": 5
                }]
            }]
        }]

        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as f:
            json.dump(conflict_manifest, f)
            temp_path = f.name

        try:
            # Check-only must detect and report the conflict
            out_check = StringIO()
            call_command('import_catalogue', fixture=temp_path, check_only=True, stdout=out_check)
            check_output = out_check.getvalue()
            self.assertIn('Detected Conflicts (1):', check_output)
            self.assertIn('front_content', check_output)
            self.assertIn('order', check_output)

            # Import without --overwrite-conflicts must preserve existing content
            out_import = StringIO()
            call_command('import_catalogue', fixture=temp_path, stdout=out_import)
            import_output = out_import.getvalue()
            self.assertIn('[CONFLICT]', import_output)
            self.assertIn('Preserved existing', import_output)

            # Assert database record was NOT overwritten
            capsule.refresh_from_db()
            self.assertEqual(capsule.front_content, "Original DB Front Content")
            self.assertEqual(capsule.back_content, "Original DB Back Content")
            self.assertEqual(capsule.order, 0)
        finally:
            Path(temp_path).unlink(missing_ok=True)

    def test_existing_quiz_conflict_reported_and_preserved(self):
        import tempfile
        import json
        from pathlib import Path
        from django.core.management import call_command
        from io import StringIO

        subject = Subject.objects.create(name="Quiz Test Course", description="Desc")
        topic = Topic.objects.create(subject=subject, title="Quiz Topic", order=0)
        capsule = Capsule.objects.create(
            topic=topic,
            title="Quiz Capsule",
            front_content="Front",
            back_content="Back",
            order=0
        )
        quiz_q = QuizQuestion.objects.create(
            capsule=capsule,
            prompt="What is 2 + 2?",
            option_a="3",
            option_b="4",
            option_c="5",
            option_d="6",
            correct_option="B",
            explanation="2 + 2 equals 4.",
            kids_hint="Count on your fingers!"
        )

        conflict_manifest = [{
            "name": "Quiz Test Course",
            "topics": [{
                "title": "Quiz Topic",
                "capsules": [{
                    "title": "Quiz Capsule",
                    "front_content": "Front",
                    "back_content": "Back",
                    "order": 0,
                    "quiz": {
                        "prompt": "What is 2 + 2?",
                        "option_a": "Changed Option A",
                        "option_b": "Changed Option B",
                        "option_c": "Changed Option C",
                        "option_d": "Changed Option D",
                        "correct_option": "A",
                        "explanation": "Different explanation.",
                        "kids_hint": "New hint"
                    }
                }]
            }]
        }]

        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as f:
            json.dump(conflict_manifest, f)
            temp_path = f.name

        try:
            # Check-only detects quiz differences
            out_check = StringIO()
            call_command('import_catalogue', fixture=temp_path, check_only=True, stdout=out_check)
            self.assertIn("Quiz on Capsule 'Quiz Capsule': Existing question differs in", out_check.getvalue())

            # Normal import does NOT silently retain or overwrite without reporting
            out_import = StringIO()
            call_command('import_catalogue', fixture=temp_path, stdout=out_import)
            self.assertIn('[CONFLICT]', out_import.getvalue())
            self.assertIn('Preserved existing', out_import.getvalue())

            # Verify existing values are preserved
            quiz_q.refresh_from_db()
            self.assertEqual(quiz_q.correct_option, "B")
            self.assertEqual(quiz_q.option_a, "3")

            # With --overwrite-conflicts, updates are applied
            out_overwrite = StringIO()
            call_command('import_catalogue', fixture=temp_path, overwrite_conflicts=True, stdout=out_overwrite)
            self.assertIn('[OVERWRITTEN]', out_overwrite.getvalue())

            quiz_q.refresh_from_db()
            self.assertEqual(quiz_q.correct_option, "A")
            self.assertEqual(quiz_q.option_a, "Changed Option A")
        finally:
            Path(temp_path).unlink(missing_ok=True)

    def test_invalid_manifest_fails_validation_before_writes(self):
        import tempfile
        import json
        from pathlib import Path
        from django.core.management import call_command, CommandError

        invalid_manifest = [{
            "name": "Invalid Course",
            "topics": [{
                "title": "Invalid Topic",
                "capsules": [{
                    "title": "Invalid Capsule",
                    "front_content": "Front",
                    "back_content": "Back",
                    "quiz": {
                        "prompt": "Invalid Q",
                        "option_a": "A",
                        "option_b": "B",
                        "option_c": "C",
                        "option_d": "D",
                        "correct_option": "Z",
                        "explanation": "Exp"
                    }
                }]
            }]
        }]

        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as f:
            json.dump(invalid_manifest, f)
            temp_path = f.name

        try:
            with self.assertRaises(CommandError) as ctx:
                call_command('import_catalogue', fixture=temp_path)
            self.assertIn("invalid correct_option 'Z'", str(ctx.exception))

            # Database should not have created 'Invalid Course'
            self.assertFalse(Subject.objects.filter(name="Invalid Course").exists())
        finally:
            Path(temp_path).unlink(missing_ok=True)

    def test_transaction_rollback_on_failure(self):
        import tempfile
        import json
        from pathlib import Path
        from unittest.mock import patch
        from django.core.management import call_command

        manifest = [{
            "name": "Rollback Test Course",
            "topics": [{
                "title": "Rollback Topic",
                "capsules": [{
                    "title": "Rollback Capsule",
                    "front_content": "Front",
                    "back_content": "Back"
                }]
            }]
        }]

        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as f:
            json.dump(manifest, f)
            temp_path = f.name

        try:
            # Simulate an unhandled database error during capsule creation
            with patch.object(Capsule.objects, 'create', side_effect=RuntimeError("Simulated DB Crash")):
                with self.assertRaises(RuntimeError):
                    call_command('import_catalogue', fixture=temp_path)

            # Atomic transaction must roll back Subject and Topic creations
            self.assertFalse(Subject.objects.filter(name="Rollback Test Course").exists())
            self.assertFalse(Topic.objects.filter(title="Rollback Topic").exists())
        finally:
            Path(temp_path).unlink(missing_ok=True)

    def test_pwa_manifest_and_sw_endpoints(self):
        client = Client()
        manifest_res = client.get(reverse('manifest'))
        self.assertEqual(manifest_res.status_code, 200)
        self.assertIn('application/manifest+json', manifest_res['Content-Type'])

        sw_res = client.get(reverse('service_worker'))
        self.assertEqual(sw_res.status_code, 200)
        self.assertIn('educaps-v4', sw_res.content.decode('utf-8'))

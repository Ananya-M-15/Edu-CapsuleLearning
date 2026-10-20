import math
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# Represents a broad subject
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    icon_class = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., 'fas fa-piggy-bank' from Font Awesome")
    subscribers = models.ManyToManyField(User, related_name='subscribed_subjects', blank=True)

    def __str__(self):
        return self.name


# Represents a specific topic within a Subject
class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=150)
    order = models.PositiveIntegerField(default=0, help_text="Order of topics within a subject.")

    class Meta:
        ordering = ['subject__name', 'order']

    def __str__(self):
        return f"{self.subject.name} - {self.title}"


# A Capsule is a small part of a Topic
class Capsule(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='capsules')
    title = models.CharField(max_length=200)
    front_content = models.TextField(help_text="Content for the front of the flip card.")
    back_content = models.TextField(help_text="Content for the back of the flip card.")
    order = models.PositiveIntegerField(default=0, help_text="Order of capsules within a topic (Day 1, Day 2, etc.).")

    class Meta:
        ordering = ['topic__order', 'order']

    def __str__(self):
        return self.title


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    capsule = models.ForeignKey(Capsule, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'capsule')

    def __str__(self):
        return f"{self.user.username} completed {self.capsule.title}"


# ============================================================================
# SPRINT EXTENSIONS: LEARNER PROFILES, QUIZZES & SPACED REPETITION
# ============================================================================

class LearnerProfile(models.Model):
    """
    Persistent profile linked 1-to-1 with the Django User.
    Stores learning mode ('standard' or 'kids'), streak counts, and activity metrics.
    """
    MODE_STANDARD = 'standard'
    MODE_KIDS = 'kids'
    MODE_CHOICES = [
        (MODE_STANDARD, 'Standard Mode'),
        (MODE_KIDS, 'Kids Mode'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    learner_mode = models.CharField(max_length=20, choices=MODE_CHOICES, default=MODE_STANDARD)
    mode_chosen = models.BooleanField(default=False, help_text="True if user has explicitly confirmed their mode selection.")
    streak_count = models.PositiveIntegerField(default=0)
    last_active_date = models.DateField(null=True, blank=True)
    daily_goal_capsules = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"{self.user.username} ({self.get_learner_mode_display()})"

    @property
    def is_kids_mode(self):
        return self.learner_mode == self.MODE_KIDS

    @property
    def mentor_name(self):
        return "Cappy" if self.is_kids_mode else "Anaya"

    @property
    def mentor_title(self):
        return "Your 3D Robot Mascot & Learning Guide" if self.is_kids_mode else "Your Strategic Career & Learning Mentor"

    @property
    def mentor_image(self):
        return "images/mentors/cappy.jpg" if self.is_kids_mode else "images/mentors/anaya.jpg"

    @property
    def mentor_greeting(self):
        if self.is_kids_mode:
            return "Beep-boop! Hey there, explorer! I'm Cappy, your robot guide! Ready for another fun learning adventure today?"
        return "Welcome! I'm Anaya, your learning and career mentor. Let's master focused micro-skills and build lasting knowledge together."


@receiver(post_save, sender=User)
def create_or_save_learner_profile(sender, instance, created, **kwargs):
    """
    Ensures every Django user automatically has an associated LearnerProfile.
    Handles legacy users safely via get_or_create.
    """
    if created:
        LearnerProfile.objects.create(user=instance)
    else:
        LearnerProfile.objects.get_or_create(user=instance)


class QuizQuestion(models.Model):
    """
    Topic and capsule assessment question with four multiple choice options,
    explicit correct answer key, pedagogical explanation, and a Kids Mode hint.
    """
    capsule = models.ForeignKey(Capsule, on_delete=models.CASCADE, related_name='quiz_questions')
    prompt = models.TextField(help_text="The question text presented to the learner.")
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(
        max_length=1,
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],
        help_text="The letter of the correct option (A, B, C, or D)."
    )
    explanation = models.TextField(help_text="Clear pedagogical explanation shown after answer submission.")
    kids_hint = models.CharField(max_length=255, blank=True, help_text="Friendly hint provided by Cappy in Kids Mode.")

    def __str__(self):
        return f"Quiz for {self.capsule.title}: {self.prompt[:45]}..."

    def is_correct(self, option_letter):
        if not option_letter:
            return False
        return str(option_letter).strip().upper() == self.correct_option


class UserQuizAttempt(models.Model):
    """
    Records an authenticated learner's answer attempt for weakness detection and analytics.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts')
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='attempts')
    selected_option = models.CharField(max_length=1)
    is_correct = models.BooleanField()
    attempted_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-attempted_at']

    def __str__(self):
        status = "Correct" if self.is_correct else "Incorrect"
        return f"{self.user.username} - Q{self.question.id} ({status})"


class ReviewSchedule(models.Model):
    """
    SuperMemo SM-2 Spaced Repetition engine schedule for a specific user and capsule.
    Tracks repetition count, easiness factor (EF), interval in days, and due date.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_schedules')
    capsule = models.ForeignKey(Capsule, on_delete=models.CASCADE, related_name='review_schedules')
    repetition_number = models.PositiveIntegerField(default=0)
    easiness_factor = models.FloatField(default=2.5)
    interval_days = models.PositiveIntegerField(default=1)
    next_review_date = models.DateField(default=timezone.now)
    last_reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'capsule')

    def __str__(self):
        return f"Review for {self.user.username} - {self.capsule.title} (due: {self.next_review_date})"

    def record_review(self, grade, review_date=None):
        """
        Applies the standard SuperMemo SM-2 algorithm:
        grade: integer from 0 (complete blackout) to 5 (perfect recall).
        - If grade >= 3: successful recall.
          - repetition 0 -> interval = 1 day
          - repetition 1 -> interval = 6 days
          - repetition >= 2 -> interval = ceil(previous_interval * easiness_factor)
          - increment repetition_number by 1
        - If grade < 3: failed recall.
          - repetition_number reset to 0
          - interval_days reset to 1
        - Easiness Factor update:
          EF' = max(1.3, EF + (0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02)))
        """
        if review_date is None:
            review_date = timezone.now().date()
        grade = max(0, min(5, int(grade)))

        # SM-2 Easiness Factor formula
        new_ef = self.easiness_factor + (0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02))
        self.easiness_factor = max(1.3, round(new_ef, 2))

        if grade >= 3:
            if self.repetition_number == 0:
                self.interval_days = 1
            elif self.repetition_number == 1:
                self.interval_days = 6
            else:
                self.interval_days = math.ceil(self.interval_days * self.easiness_factor)
            self.repetition_number += 1
        else:
            self.repetition_number = 0
            self.interval_days = 1

        self.next_review_date = review_date + timedelta(days=self.interval_days)
        self.last_reviewed_at = timezone.now()
        self.save()
        return self
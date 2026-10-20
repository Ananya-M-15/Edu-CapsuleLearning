from django.utils import timezone
from django.db.models import Count, Q, Avg
from .models import LearnerProfile, UserProgress, UserQuizAttempt, ReviewSchedule, Topic, Capsule


def get_or_create_learner_profile(user):
    """
    Safely retrieves or initializes a LearnerProfile for any User instance,
    guaranteeing seamless compatibility with existing legacy accounts.
    """
    profile, _ = LearnerProfile.objects.get_or_create(user=user)
    return profile


def calculate_topic_weaknesses(user):
    """
    Evaluates learner performance across all attempted quiz questions grouped by Topic.
    A topic is flagged as 'needs_review' if the learner's overall accuracy is below 70%,
    or if they have scored incorrect answers without subsequent mastery.
    """
    attempts = UserQuizAttempt.objects.filter(user=user).select_related('question__capsule__topic__subject')
    if not attempts.exists():
        return []

    topic_stats = {}
    for attempt in attempts:
        topic = attempt.question.capsule.topic
        if topic.id not in topic_stats:
            topic_stats[topic.id] = {
                'topic': topic,
                'subject': topic.subject,
                'total_attempts': 0,
                'correct_attempts': 0,
            }
        topic_stats[topic.id]['total_attempts'] += 1
        if attempt.is_correct:
            topic_stats[topic.id]['correct_attempts'] += 1

    weakness_reports = []
    for tid, data in topic_stats.items():
        total = data['total_attempts']
        correct = data['correct_attempts']
        accuracy = round((correct / total) * 100) if total > 0 else 0
        needs_review = accuracy < 70 or (total - correct) >= 2

        weakness_reports.append({
            'topic': data['topic'],
            'subject': data['subject'],
            'total_attempts': total,
            'correct_attempts': correct,
            'accuracy': accuracy,
            'needs_review': needs_review,
        })

    # Sort so topics with the lowest accuracy appear first
    weakness_reports.sort(key=lambda x: (not x['needs_review'], x['accuracy']))
    return weakness_reports


def get_due_reviews(user):
    """
    Retrieves all capsules scheduled for spaced repetition review on or before today.
    """
    today = timezone.now().date()
    return ReviewSchedule.objects.filter(
        user=user,
        next_review_date__lte=today
    ).select_related('capsule', 'capsule__topic', 'capsule__topic__subject').order_by('next_review_date')


def get_learner_stats(user):
    """
    Aggregates learning stats: capsules completed, accuracy, active streak, and pending reviews.
    """
    profile = get_or_create_learner_profile(user)
    completed_capsules = UserProgress.objects.filter(user=user).count()

    total_attempts = UserQuizAttempt.objects.filter(user=user).count()
    correct_attempts = UserQuizAttempt.objects.filter(user=user, is_correct=True).count()
    quiz_accuracy = round((correct_attempts / total_attempts) * 100) if total_attempts > 0 else 0

    due_reviews_count = get_due_reviews(user).count()

    return {
        'profile': profile,
        'mode': profile.learner_mode,
        'is_kids_mode': profile.is_kids_mode,
        'mentor_name': profile.mentor_name,
        'mentor_title': profile.mentor_title,
        'mentor_image': profile.mentor_image,
        'mentor_greeting': profile.mentor_greeting,
        'completed_capsules': completed_capsules,
        'total_attempts': total_attempts,
        'quiz_accuracy': quiz_accuracy,
        'due_reviews_count': due_reviews_count,
        'streak_count': profile.streak_count,
        'daily_goal': profile.daily_goal_capsules,
    }

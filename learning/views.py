import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.db.models import Count, Q
from django.utils import timezone

from .forms import SignUpForm
from .models import Subject, Topic, Capsule, UserProgress, LearnerProfile, QuizQuestion, UserQuizAttempt, ReviewSchedule
from .services import get_or_create_learner_profile, calculate_topic_weaknesses, get_due_reviews, get_learner_stats
from .ai_tutor import explain_capsule, generate_quiz_hint, answer_capsule_query, get_dashboard_briefing, get_mentor_persona


# ============================================================================
# PUBLIC HOMEPAGE & AUTHENTICATION
# ============================================================================

def home_view(request):
    """
    Public landing page for EduCaps introducing micro-learning, both learner modes,
    and the approved 3D mentors (Cappy and Anaya). Accessible to all visitors.
    Authenticated users retain an obvious route to their personalized dashboard.
    """
    subjects = Subject.objects.prefetch_related('topics__capsules').annotate(
        total_capsules=Count('topics__capsules', distinct=True),
        total_topics=Count('topics', distinct=True)
    ).all()
    total_capsules = Capsule.objects.count()
    total_subjects = Subject.objects.count()

    profile = None
    enrolled_subjects = []
    if request.user.is_authenticated:
        profile = get_or_create_learner_profile(request.user)
        enrolled_subjects = request.user.subscribed_subjects.all()

    context = {
        'subjects': subjects,
        'total_capsules': total_capsules,
        'total_subjects': total_subjects,
        'profile': profile,
        'enrolled_subjects': enrolled_subjects,
        'cappy_mentor': get_mentor_persona('kids').to_dict(),
        'anaya_mentor': get_mentor_persona('standard').to_dict(),
    }
    return render(request, 'home.html', context)


def search_view(request):
    """
    Real database search supporting matches across Course/Subject titles,
    descriptions, topic titles, and capsule contents. Accessible to all users.
    """
    query = request.GET.get('q', '').strip()
    profile = None
    if request.user.is_authenticated:
        profile = get_or_create_learner_profile(request.user)

    if not query:
        return redirect('library')

    # Build search terms (including stem variant for common English suffixes)
    terms = [query]
    cleaned = query.lower()
    if cleaned.endswith('e') and len(cleaned) > 4:
        terms.append(cleaned[:-1])
    elif cleaned.endswith('s') and len(cleaned) > 4:
        terms.append(cleaned[:-1])
    elif cleaned.endswith('ing') and len(cleaned) > 5:
        terms.append(cleaned[:-3])

    subject_filter = Q()
    topic_filter = Q()
    for term in terms:
        subject_filter |= (
            Q(name__icontains=term) |
            Q(description__icontains=term) |
            Q(topics__title__icontains=term) |
            Q(topics__capsules__title__icontains=term) |
            Q(topics__capsules__front_content__icontains=term)
        )
        topic_filter |= (
            Q(title__icontains=term) |
            Q(subject__name__icontains=term) |
            Q(capsules__title__icontains=term) |
            Q(capsules__front_content__icontains=term)
        )

    matching_subjects = Subject.objects.filter(
        subject_filter
    ).prefetch_related('topics__capsules').annotate(
        total_capsules=Count('topics__capsules', distinct=True),
        total_topics=Count('topics', distinct=True)
    ).distinct()

    matching_topics = Topic.objects.filter(
        topic_filter
    ).select_related('subject').prefetch_related('capsules').distinct()

    total_results = matching_subjects.count() + matching_topics.count()

    context = {
        'query': query,
        'matching_subjects': matching_subjects,
        'matching_topics': matching_topics,
        'total_results': total_results,
        'profile': profile,
    }
    return render(request, 'search_results.html', context)



def signup_view(request):
    """
    User registration view with case-insensitive unique username validation,
    automatic LearnerProfile creation via signal, and automatic login.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='learning.backends.CaseInsensitiveModelBackend')
            # Redirect first-time users to mode selection
            return redirect('select_mode')
        return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# ============================================================================
# LEARNER PROFILE & MODE SELECTION
# ============================================================================

@login_required
def select_mode_view(request):
    """
    Allows a learner to choose between Standard Mode (Anaya) and Kids Mode (Cappy).
    """
    profile = get_or_create_learner_profile(request.user)

    if request.method == 'POST':
        chosen_mode = request.POST.get('mode')
        if chosen_mode in [LearnerProfile.MODE_STANDARD, LearnerProfile.MODE_KIDS]:
            profile.learner_mode = chosen_mode
            profile.mode_chosen = True
            profile.save()
            next_url = request.POST.get('next') or request.GET.get('next') or 'dashboard'
            return redirect(next_url)

    context = {
        'profile': profile,
        'current_mode': profile.learner_mode,
        'cappy': get_mentor_persona('kids').to_dict(),
        'anaya': get_mentor_persona('standard').to_dict(),
        'next': request.GET.get('next', 'dashboard'),
    }
    return render(request, 'select_mode.html', context)


@login_required
@require_POST
def toggle_mode_view(request):
    """
    Instant switch between Standard Mode and Kids Mode from navigation or settings.
    """
    profile = get_or_create_learner_profile(request.user)
    if profile.learner_mode == LearnerProfile.MODE_KIDS:
        profile.learner_mode = LearnerProfile.MODE_STANDARD
    else:
        profile.learner_mode = LearnerProfile.MODE_KIDS
    profile.save()

    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    return redirect('dashboard')


# ============================================================================
# PERSONALIZED DASHBOARD & LEARNING
# ============================================================================

@login_required
def dashboard(request):
    """
    Unified personalized learning hub:
    - Overall completion metrics and progress bars
    - Continue-learning action pointing directly to next uncompleted capsule
    - Course discovery (enrolled vs discoverable subjects)
    - Mode-specific AI mentor card (Cappy or Anaya)
    - Topics needing review (weakness detection) and due spaced reviews
    """
    profile = get_or_create_learner_profile(request.user)
    subscribed_subjects = request.user.subscribed_subjects.all()

    stats = get_learner_stats(request.user)

    # Base progress calculations
    if not subscribed_subjects.exists():
        all_subjects = Subject.objects.all()
        context = {
            'completed_count': 0,
            'total_capsules': 0,
            'remaining_count': 0,
            'progress_percentage': 0,
            'no_subscriptions': True,
            'profile': profile,
            'is_kids_mode': profile.is_kids_mode,
            'discover_subjects': all_subjects,
            'stats': stats,
            'briefing': get_dashboard_briefing(request.user, mode=profile.learner_mode),
        }
        return render(request, 'dashboard.html', context)

    total_capsules = Capsule.objects.filter(topic__subject__in=subscribed_subjects).count()
    completed_count = UserProgress.objects.filter(
        user=request.user,
        capsule__topic__subject__in=subscribed_subjects
    ).count()
    remaining_count = max(0, total_capsules - completed_count)
    progress_percentage = round((completed_count / total_capsules) * 100) if total_capsules > 0 else 0

    # Next uncompleted capsule for Continue Learning CTA
    completed_ids = set(UserProgress.objects.filter(user=request.user).values_list('capsule_id', flat=True))
    next_capsule = Capsule.objects.filter(
        topic__subject__in=subscribed_subjects
    ).exclude(id__in=completed_ids).first()

    # Enrolled subjects with progress
    enrolled_subjects = Subject.objects.filter(id__in=subscribed_subjects.values_list('id', flat=True)).annotate(
        total_capsules_count=Count('topics__capsules', distinct=True),
        completed_capsules_count=Count(
            'topics__capsules',
            filter=Q(topics__capsules__userprogress__user=request.user),
            distinct=True
        )
    )

    # Discoverable subjects (not yet subscribed)
    discover_subjects = Subject.objects.exclude(id__in=subscribed_subjects.values_list('id', flat=True))

    # Weaknesses & spaced reviews
    weaknesses = calculate_topic_weaknesses(request.user)
    topics_needing_review = [w for w in weaknesses if w['needs_review']][:3]
    due_reviews = get_due_reviews(request.user)[:4]

    stats = get_learner_stats(request.user)
    briefing = get_dashboard_briefing(request.user, mode=profile.learner_mode)

    context = {
        'completed_count': completed_count,
        'total_capsules': total_capsules,
        'progress_percentage': progress_percentage,
        'remaining_count': remaining_count,
        'no_subscriptions': False,
        'next_capsule': next_capsule,
        'enrolled_subjects': enrolled_subjects,
        'discover_subjects': discover_subjects,
        'profile': profile,
        'is_kids_mode': profile.is_kids_mode,
        'stats': stats,
        'briefing': briefing,
        'topics_needing_review': topics_needing_review,
        'due_reviews': due_reviews,
    }
    return render(request, 'dashboard.html', context)


@login_required
def learn_view(request):
    """
    Main lesson screen:
    - Interactive flip card (front/back) with mobile touch support
    - Mode-specific AI mentor explanation (Cappy or Anaya)
    - Interactive quiz question and feedback
    - Dynamic tutor question-asking drawer
    """
    profile = get_or_create_learner_profile(request.user)
    subscribed_subjects = request.user.subscribed_subjects.all()

    if not subscribed_subjects.exists():
        return render(request, 'subscribe_prompt.html')

    # Allow query param ?capsule_id=... to review a specific capsule
    capsule_id = request.GET.get('capsule_id')
    if capsule_id:
        capsule = get_object_or_404(Capsule, id=capsule_id)
    else:
        completed_capsule_ids = UserProgress.objects.filter(user=request.user).values_list('capsule_id', flat=True)
        capsule = Capsule.objects.filter(
            topic__subject__in=subscribed_subjects
        ).exclude(id__in=completed_capsule_ids).first()

    if not capsule:
        return render(request, 'all_completed.html')

    is_completed = UserProgress.objects.filter(user=request.user, capsule=capsule).exists()
    explanation = explain_capsule(capsule, mode=profile.learner_mode)
    quiz_questions = capsule.quiz_questions.all()

    context = {
        'capsule': capsule,
        'topic': capsule.topic,
        'is_completed': is_completed,
        'profile': profile,
        'is_kids_mode': profile.is_kids_mode,
        'mentor_persona': get_mentor_persona(profile.learner_mode).to_dict(),
        'explanation': explanation,
        'quiz_questions': quiz_questions,
    }
    return render(request, 'learn.html', context)


@login_required
@require_POST
def complete_capsule_view(request, capsule_id):
    """
    Marks a capsule as completed for the authenticated user and initializes SM-2 review schedule.
    """
    capsule = get_object_or_404(Capsule, id=capsule_id)
    UserProgress.objects.get_or_create(user=request.user, capsule=capsule)

    # Initialize review schedule if not already present
    ReviewSchedule.objects.get_or_create(user=request.user, capsule=capsule)

    # Update profile streak / last active
    profile = get_or_create_learner_profile(request.user)
    today = timezone.now().date()
    if profile.last_active_date != today:
        profile.streak_count += 1
        profile.last_active_date = today
        profile.save()

    return JsonResponse({'status': 'success', 'message': 'Progress saved!'})


# ============================================================================
# INTERACTIVE QUIZ & AI TUTOR ENDPOINTS
# ============================================================================

@login_required
@require_POST
def submit_quiz_view(request, question_id):
    """
    Evaluates a learner's quiz answer, persists the attempt, updates SM-2 schedule,
    and returns explanatory feedback and progressive hints.
    """
    question = get_object_or_404(QuizQuestion, id=question_id)
    selected_option = request.POST.get('selected_option', '').strip().upper()

    if not selected_option:
        return JsonResponse({'status': 'error', 'message': 'Please select an answer.'}, status=400)

    is_correct = question.is_correct(selected_option)

    # Persist attempt
    UserQuizAttempt.objects.create(
        user=request.user,
        question=question,
        selected_option=selected_option,
        is_correct=is_correct
    )

    # Update SM-2 schedule for capsule (grade 5 if correct, grade 2 if incorrect)
    schedule, _ = ReviewSchedule.objects.get_or_create(user=request.user, capsule=question.capsule)
    grade = 5 if is_correct else 2
    schedule.record_review(grade=grade)

    profile = get_or_create_learner_profile(request.user)
    hint = generate_quiz_hint(question, mode=profile.learner_mode)

    return JsonResponse({
        'status': 'success',
        'is_correct': is_correct,
        'correct_option': question.correct_option,
        'explanation': question.explanation,
        'hint': hint,
        'mentor_name': profile.mentor_name,
        'next_review_days': schedule.interval_days,
    })


@login_required
@require_POST
def tutor_ask_view(request, capsule_id):
    """
    Accepts learner queries about the current capsule and provides grounded,
    mode-specific answers from Cappy (Kids) or Anaya (Standard).
    """
    capsule = get_object_or_404(Capsule, id=capsule_id)
    query = request.POST.get('query', '').strip()

    profile = get_or_create_learner_profile(request.user)
    answer = answer_capsule_query(capsule, query, mode=profile.learner_mode)

    return JsonResponse({
        'status': 'success',
        'mentor': answer['mentor'],
        'response': answer['response'],
    })


# ============================================================================
# SPACED REPETITION & LIBRARY BROWSING
# ============================================================================

@login_required
def reviews_view(request):
    """
    Spaced repetition revision dashboard displaying due reviews and practice queues.
    """
    profile = get_or_create_learner_profile(request.user)
    due_reviews = get_due_reviews(request.user)
    all_schedules = ReviewSchedule.objects.filter(user=request.user).select_related('capsule__topic__subject')
    weaknesses = calculate_topic_weaknesses(request.user)

    context = {
        'profile': profile,
        'is_kids_mode': profile.is_kids_mode,
        'due_reviews': due_reviews,
        'all_schedules': all_schedules,
        'weaknesses': weaknesses,
    }
    return render(request, 'reviews.html', context)


def subject_library_view(request):
    """
    Library view displaying all subjects, topics, and completion status.
    Accessible to all users; personalizes progress indicators for authenticated learners.
    Supports optional search filter query 'q' for catalog scalability.
    """
    profile = None
    completed_capsule_ids = set()
    query = request.GET.get('q', '').strip()

    subject_filter = Q()
    if query:
        subject_filter = (
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(topics__title__icontains=query) |
            Q(topics__capsules__title__icontains=query) |
            Q(topics__capsules__front_content__icontains=query)
        )

    if request.user.is_authenticated:
        profile = get_or_create_learner_profile(request.user)
        subjects = Subject.objects.filter(subject_filter).prefetch_related(
            'topics__capsules'
        ).annotate(
            total_capsules_in_subject=Count('topics__capsules', distinct=True),
            completed_capsules_in_subject=Count(
                'topics__capsules',
                filter=Q(topics__capsules__userprogress__user=request.user),
                distinct=True
            )
        ).order_by('id').distinct()
        topics = Topic.objects.annotate(
            total_capsules=Count('capsules', distinct=True),
            completed_capsules=Count('capsules', filter=Q(capsules__userprogress__user=request.user), distinct=True)
        )
        completed_capsule_ids = set(
            UserProgress.objects.filter(user=request.user).values_list('capsule_id', flat=True)
        )
    else:
        subjects = Subject.objects.filter(subject_filter).prefetch_related(
            'topics__capsules'
        ).annotate(
            total_capsules_in_subject=Count('topics__capsules', distinct=True),
            completed_capsules_in_subject=Count('id', filter=Q(id__lt=0))
        ).order_by('id').distinct()
        topics = Topic.objects.annotate(
            total_capsules=Count('capsules', distinct=True),
            completed_capsules=Count('id', filter=Q(id__lt=0))
        )

    context = {
        'subjects': subjects,
        'topics_with_progress': {topic.id: topic for topic in topics},
        'completed_capsule_ids': completed_capsule_ids,
        'profile': profile,
        'is_kids_mode': profile.is_kids_mode if profile else False,
        'query': query,
    }
    return render(request, 'library.html', context)


@login_required
def my_learning_view(request):
    """
    Displays only courses enrolled in by the authenticated user.
    """
    profile = get_or_create_learner_profile(request.user)
    enrolled_subjects = request.user.subscribed_subjects.all().order_by('id')
    subscribed_subject_ids = list(enrolled_subjects.values_list('id', flat=True))

    context = {
        'enrolled_subjects': enrolled_subjects,
        'all_subjects': enrolled_subjects,  # backwards-compatibility
        'subscribed_subject_ids': subscribed_subject_ids,
        'profile': profile,
        'is_kids_mode': profile.is_kids_mode,
    }
    return render(request, 'my_learning.html', context)


@login_required
@require_POST
def toggle_subscription_view(request, subject_id):
    """
    Toggles subject enrollment for the authenticated user.
    """
    subject = get_object_or_404(Subject, id=subject_id)
    user = request.user

    if subject in user.subscribed_subjects.all():
        user.subscribed_subjects.remove(subject)
    else:
        user.subscribed_subjects.add(subject)

    return redirect('my_learning')


# ============================================================================
# PWA MANIFEST & SERVICE WORKER
# ============================================================================

def manifest_view(request):
    """
    Web App Manifest providing PWA installability on desktop and mobile browsers.
    """
    manifest_data = {
        "name": "EduCaps - Daily Micro-Learning",
        "short_name": "EduCaps",
        "description": "Bite-sized daily micro-learning with 3D AI mentors Cappy and Anaya.",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#0f172a",
        "theme_color": "#8b5cf6",
        "orientation": "portrait-primary",
        "icons": [
            {
                "src": "/static/images/icon-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": "/static/images/icon-512x512.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable"
            }
        ]
    }
    return HttpResponse(json.dumps(manifest_data), content_type="application/manifest+json")


def service_worker_view(request):
    """
    Safe PWA Service Worker caching core CSS and assets while using Network-First
    for dynamic authenticated views to avoid serving stale learner data.
    """
    sw_code = """
const CACHE_NAME = 'educaps-v4';
const STATIC_ASSETS = [
    '/static/css/style.css',
    '/static/js/main.js',
    '/static/images/mentors/cappy.jpg',
    '/static/images/mentors/anaya.jpg'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS))
    );
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => Promise.all(
            keys.map((k) => {
                if (k !== CACHE_NAME) return caches.delete(k);
            })
        ))
    );
    self.clients.claim();
});

self.addEventListener('fetch', (event) => {
    // Only intercept GET requests
    if (event.request.method !== 'GET') return;

    // Cache static assets with cache-first strategy
    if (event.request.url.includes('/static/')) {
        event.respondWith(
            caches.match(event.request).then((cached) => cached || fetch(event.request))
        );
        return;
    }

    // Dynamic routes use Network-First to never serve stale learner progress
    event.respondWith(
        fetch(event.request).catch(() => caches.match(event.request))
    );
});
"""
    return HttpResponse(sw_code, content_type="application/javascript")
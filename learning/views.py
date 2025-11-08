from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import SignUpForm

# FIXED IMPORTS START
from .models import Subject, Topic, Capsule, UserProgress 
from django.db.models import Count, Q

# View for the signup page
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# View for the user's dashboard page
@login_required
def dashboard(request):
    subscribed_subjects = request.user.subscribed_subjects.all()

    if not subscribed_subjects.exists():
        context = {
            'completed_count': 0,
            'total_capsules': 0,
            'remaining_count': 0,
            'progress_percentage': 0,
            'no_subscriptions': True, 
        }
        return render(request, 'dashboard.html', context)

    # CALCULATIONS ARE NOW PERSONALIZED 
    total_capsules = Capsule.objects.filter(topic__subject__in=subscribed_subjects).count()
    completed_count = UserProgress.objects.filter(
        user=request.user,
        capsule__topic__subject__in=subscribed_subjects
    ).count()
    remaining_count = total_capsules - completed_count
    
    if total_capsules > 0:
        progress_percentage = round((completed_count / total_capsules) * 100)
    else:
        progress_percentage = 0
        
    context = {
        'completed_count': completed_count,
        'total_capsules': total_capsules,
        'progress_percentage': progress_percentage,
        'remaining_count': remaining_count,
    }
    return render(request, 'dashboard.html', context)

# View for the main learning page with the flip card
@login_required
def learn_view(request):
    subscribed_subjects = request.user.subscribed_subjects.all()
    
    if not subscribed_subjects.exists():
        return render(request, 'subscribe_prompt.html')

    completed_capsule_ids = UserProgress.objects.filter(user=request.user).values_list('capsule_id', flat=True)
    
    # Find the next capsule:
    next_capsule = Capsule.objects.filter(
        topic__subject__in=subscribed_subjects
    ).exclude(
        id__in=completed_capsule_ids
    ).first() 
    
    if not next_capsule:
        return render(request, 'all_completed.html')

    return render(request, 'learn.html', {'capsule': next_capsule, 'topic': next_capsule.topic})

# Handles the request when the "Mark as Complete" button is clicked
@login_required
@require_POST
def complete_capsule_view(request, capsule_id):
    capsule = Capsule.objects.get(id=capsule_id)
    UserProgress.objects.get_or_create(user=request.user, capsule=capsule)
    return JsonResponse({'status': 'success', 'message': 'Progress saved!'})


# View for the new Subject Library page
@login_required
def subject_library_view(request):
    subjects = Subject.objects.prefetch_related(
        'topics__capsules' 
    ).annotate(
        total_capsules_in_subject=Count('topics__capsules'),
        completed_capsules_in_subject=Count(
            'topics__capsules',
            filter=Q(topics__capsules__userprogress__user=request.user)
        )
    )

    # topic-specific progress
    topics = Topic.objects.annotate(
        total_capsules=Count('capsules'),
        completed_capsules=Count('capsules', filter=Q(capsules__userprogress__user=request.user))
    )

    completed_capsule_ids = set(
        UserProgress.objects.filter(user=request.user).values_list('capsule_id', flat=True)
    )

    context = {
        'subjects': subjects,
        'topics_with_progress': {topic.id: topic for topic in topics},
        'completed_capsule_ids': completed_capsule_ids, # <-- Pass the list to the template
    }
    return render(request, 'library.html', context)
@login_required
def my_learning_view(request):
    all_subjects = Subject.objects.all()
    subscribed_subject_ids = request.user.subscribed_subjects.values_list('id', flat=True)
    
    context = {
        'all_subjects': all_subjects,
        'subscribed_subject_ids': subscribed_subject_ids,
    }
    return render(request, 'my_learning.html', context)


@login_required
@require_POST 
def toggle_subscription_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    user = request.user
    
    if subject in user.subscribed_subjects.all():
        user.subscribed_subjects.remove(subject)
    else:
        user.subscribed_subjects.add(subject)
        
    # Redirect back to the "My Learning" page
    return redirect('my_learning')
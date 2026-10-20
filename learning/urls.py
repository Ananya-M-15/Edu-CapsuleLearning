from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Public & Core Learning Views
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('library/', views.subject_library_view, name='library'),
    path('search/', views.search_view, name='search'),
    path('learn/', views.learn_view, name='learn'),
    path('subscribe/<int:subject_id>/', views.toggle_subscription_view, name='toggle_subscription'),
    path('my-learning/', views.my_learning_view, name='my_learning'),
    path('complete_capsule/<int:capsule_id>/', views.complete_capsule_view, name='complete_capsule'),
    path('reviews/', views.reviews_view, name='reviews'),

    # Learner Mode & Profile Views
    path('select-mode/', views.select_mode_view, name='select_mode'),
    path('toggle-mode/', views.toggle_mode_view, name='toggle_mode'),

    # Interactive Quiz & AI Tutor APIs
    path('quiz/submit/<int:question_id>/', views.submit_quiz_view, name='submit_quiz'),
    path('tutor/ask/<int:capsule_id>/', views.tutor_ask_view, name='tutor_ask'),

    # Authentication Views
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),

    # PWA Endpoints
    path('manifest.json', views.manifest_view, name='manifest'),
    path('sw.js', views.service_worker_view, name='service_worker'),
]
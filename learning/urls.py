from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Main App Views
    path('', views.dashboard, name='dashboard'),
    path('library/', views.subject_library_view, name='library'),
    path('learn/', views.learn_view, name='learn'),
    path('subscribe/<int:subject_id>/', views.toggle_subscription_view, name='toggle_subscription'),
    path('my-learning/', views.my_learning_view, name='my_learning'),
    path('complete_capsule/<int:capsule_id>/', views.complete_capsule_view, name='complete_capsule'),
    
    # Authentication Views
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
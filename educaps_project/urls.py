from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning.urls')),  # This tells the project to look at learning/urls.py
]
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# NEW MODEL: Represents a broad subject 
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    icon_class = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., 'fas fa-piggy-bank' from Font Awesome")
    subscribers = models.ManyToManyField(User, related_name='subscribed_subjects', blank=True)
    
    def __str__(self):
        return self.name

# NEW MODEL: Represents a specific topic within a Subject
class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=150)
    order = models.PositiveIntegerField(default=0, help_text="Order of topics within a subject.")

    class Meta:
        ordering = ['subject__name', 'order'] 

    def __str__(self):
        return f"{self.subject.name} - {self.title}"


# UPDATED MODEL: A Capsule is a small part of a Topic
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
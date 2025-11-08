from django.contrib import admin
from .models import Subject, Topic, Capsule, UserProgress

# Allows to show Capsules directly inside the Topic admin page
class CapsuleInline(admin.TabularInline):
    model = Capsule
    extra = 1 

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'order')
    list_filter = ('subject',)
    inlines = [CapsuleInline] 

@admin.register(Capsule)
class CapsuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'order')
    list_filter = ('topic__subject', 'topic')
    search_fields = ('title', 'front_content', 'back_content')

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'capsule', 'completed_at')
    list_filter = ('user',)
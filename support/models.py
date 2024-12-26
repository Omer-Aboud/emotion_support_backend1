from django.db import models
from django.utils.timezone import now

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now)

class Interaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)
    emotion_detected = models.CharField(max_length=50, null=True, blank=True)
    response_generated = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

class EmotionTimeline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=50)
    logged_at = models.DateTimeField(default=now)

class Resource(models.Model):
    resource_type = models.CharField(max_length=50)
    emotion_tag = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preference_type = models.CharField(max_length=50)
    preference_value = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(default=now)

class SharedEmotionalSpace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.IntegerField()
    emotion_tag = models.CharField(max_length=50, null=True, blank=True)
    joined_at = models.DateTimeField(default=now)

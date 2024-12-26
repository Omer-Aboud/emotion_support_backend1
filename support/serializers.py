from rest_framework import serializers
from .models import User, Interaction, EmotionTimeline, Resource, UserPreference, SharedEmotionalSpace

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'

class EmotionTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionTimeline
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = '__all__'

class SharedEmotionalSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedEmotionalSpace
        fields = '__all__'

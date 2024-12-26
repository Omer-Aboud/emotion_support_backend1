from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User, Interaction, EmotionTimeline, Resource, UserPreference, SharedEmotionalSpace
from .serializers import UserSerializer, InteractionSerializer, EmotionTimelineSerializer, ResourceSerializer, UserPreferenceSerializer, SharedEmotionalSpaceSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer


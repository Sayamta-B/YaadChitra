from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Event
from .serializers import EventSerializer

class EventListCreateView(ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class EventDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'public_id'

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

class PublicEventDetailView(generics.RetrieveAPIView):
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    lookup_field = 'public_id'

    def get_queryset(self):
        return Event.objects.filter(
            view_permission__in=['public', 'link']
        )

class PublicEventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        print("PUBLIC EVENT VIEW CALLED")
        print(Event.objects.filter(view_permission='public').count())
        return Event.objects.filter(view_permission='public')
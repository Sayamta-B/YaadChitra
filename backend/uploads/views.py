from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.utils import timezone

from events.models import Event, EventGuest
from .models import Upload
from .serializers import UploadSerializer


# Find the event using its UUID.
# Check whether uploads are enabled.
# Check whether the upload deadline has passed.
# Verify that the guest belongs to this event.
# Save the uploaded file and associate it with the event and guest.

class GuestUploadView(generics.CreateAPIView):
    serializer_class = UploadSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        event = get_object_or_404(
            Event,
            public_id=self.kwargs['public_id'],
            view_permission__in=['public', 'link']
        )

        if event.upload_permission == 'disabled':
            raise ValidationError("Uploads are disabled for this event")

        if event.upload_expiry and timezone.now()>event.upload_expiry:
            raise ValidationError("The upload period has expired.")

        guest = get_object_or_404(
            EventGuest,
            id=self.request.data.get('guest_id'),
            event=event
        )

        uploaded_file = self.request.FILES.get('file')

        if not uploaded_file:
            raise ValidationError("Please provide a file.")

        serializer.save(
            event=event,
            uploaded_by=guest,
            name=uploaded_file.name,
            file_size= uploaded_file.size
        )

class EventUploadListView(generics.ListAPIView):
    serializer_class = UploadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Upload.objects.filter(
            event__public_id=self.kwargs['public_id'],
            event__organizer=self.request.user,
            is_deleted=False
        )

class UploadDetailView(generics.RetrieveAPIView):
    serializer_class = UploadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Upload.objects.filter(
            event__organizer=self.request.user,
            is_deleted=False
        )
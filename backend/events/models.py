import uuid

from django.db import models
from django.conf import settings

class Event(models.Model):
    class ViewPermission(models.TextChoices):
        PUBLIC = "public", "Public"
        LINK = "link", "Anyone with the link"
        # RESTRICTED = "restricted", "Restricted"

    class UploadPermission(models.TextChoices):
        DISABLED = "disabled", "Disabled"
        PUBLIC = "public", "Public"
        LINK = "link", "Anyone with the link"
        # RESTRICTED = "restricted", "Restricted"

    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    public_id =models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    start_datetime = models.DateTimeField()

    upload_expiry = models.DateTimeField(null=True, blank=True)
    view_permission = models.CharField(max_length=20, choices=ViewPermission.choices, default=ViewPermission.LINK)
    upload_permission = models.CharField(max_length=20, choices=UploadPermission.choices, default=UploadPermission.LINK)
    require_approval = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_datetime']


class EventGuest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='guests')
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.event.title})"

import uuid

from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Event(models.Model):
    class ViewPermission(models.TextChoices):
        PUBLIC = "public", "Public"
        LINK = "link", "Anyone with the link"
        REGISTERED = "registered", "Registered"

    class UploadPermission(models.TextChoices):
        DISABLED = "disabled", "Disabled"
        PUBLIC = "public", "Public"
        LINK = "link", "Anyone with the link"
        REGISTERED = "registered", "Registered"

    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    public_id =models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    tags = models.JSONField(default=list, blank=True)

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)

    upload_expiry = models.DateTimeField(null=True, blank=True)
    view_permission = models.CharField(max_length=20, choices=ViewPermission.choices, default=ViewPermission.PUBLIC)
    upload_permission = models.CharField(max_length=20, choices=UploadPermission.choices, default=UploadPermission.DISABLED)
    require_approval = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{self.public_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_datetime']


class EventGuest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='guests')
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['event', 'phone_number'],
                condition=~models.Q(phone_number=''),
                name='unique_guest_phone_number_per_event')
        ]

    def __str__(self):
        return f"{self.name} ({self.event.title})"

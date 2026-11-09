from django.db import models
from django.conf import settings

class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    duration_days = models.PositiveIntegerField()
    storage_limit_mb = models.PositiveIntegerField()
    max_events = models.PositiveIntegerField(default=1)

    allow_download = models.BooleanField(default=False)
    allow_blur_detection = models.BooleanField(default=False)
    allow_duplicate_detection = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.name


class EventSubscription(models.Model):
    class Status(models.TextChoices):
        TRIAL = "trial", "Trial"
        ACTIVE = "active", "Active"
        EXPIRED = "expired", "Expired"
        CANCELLED = "cancelled", "Cancelled"

    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='subscriptions')
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, related_name='subscriptions')
    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TRIAL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date']
        constraints = [
            # One trial ever per event
            models.UniqueConstraint(
                fields=['event'],
                condition=models.Q(status='trial'),
                name='unique_trial_per_event'
            ),

            # Only one current subscription per event
            models.UniqueConstraint(
                fields=['event'],
                condition=models.Q(status__in=['trial', 'active']),
                name='unique_current_subscription_per_event'
            ),
        ]

    def __str__(self):
        return f"{self.organizer.username} - {self.event.title} - {self.package.name}"
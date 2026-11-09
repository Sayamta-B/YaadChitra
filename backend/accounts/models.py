from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        ORANIZER = "organizer", "Organizer"

    role = models.CharField(max_length=20, choices= Role.choices, default=Role.ORANIZER)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Already have username, email, password, first_name, last_name, 
    # is_active, is_staff, is_superuser, last_login, date_joined fields from AbstractUser

    def __str__(self):
        return f"{self.username} - {self.role}"
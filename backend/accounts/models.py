from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Already have username, email, password, first_name, last_name, 
    # is_active, is_staff, is_superuser, last_login, date_joined fields from AbstractUser

    def __str__(self):
        return f"{self.username}"
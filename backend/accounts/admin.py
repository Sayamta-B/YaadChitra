
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'phone_number',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

    search_fields = ('username', 'email', 'phone_number', 'first_name', 'last_name')

    list_filter = ('is_active', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('phone_number',)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('email', 'phone_number')
        }),
    )

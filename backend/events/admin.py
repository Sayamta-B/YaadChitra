from django.contrib import admin
from .models import Event, EventGuest


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'organizer',
        'start_datetime',
        'view_permission',
        'upload_permission',
        'require_approval',
        'created_at',
    )

    list_filter = (
        'view_permission',
        'upload_permission',
        'require_approval',
        'start_datetime',
    )

    search_fields = (
        'title',
        'description',
        'organizer__username',
        'organizer__email',
    )

    readonly_fields = (
        'public_id',
        'created_at',
        'updated_at',
    )

    ordering = ('-start_datetime',)


@admin.register(EventGuest)
class EventGuestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'event',
        'created_at',
    )

    list_filter = (
        'event',
        'created_at',
    )

    search_fields = (
        'name',
        'event__title',
    )

    readonly_fields = (
        'created_at',
    )

    ordering = ('-created_at',)
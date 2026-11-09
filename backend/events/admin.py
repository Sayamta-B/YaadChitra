
from django.contrib import admin
from .models import Event, EventGuest


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'organizer',
        'start_datetime',
        'end_datetime',
        'view_permission',
        'upload_permission',
        'created_at',
    )

    search_fields = ('title', 'organizer__username')

    list_filter = (
        'view_permission',
        'upload_permission',
        'start_datetime',
    )


@admin.register(EventGuest)
class EventGuestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'event',
        'phone_number',
        'email',
        'created_at',
    )

    search_fields = ('name', 'phone_number', 'email')
    list_filter = ('event',)


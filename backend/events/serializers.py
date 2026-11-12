from rest_framework import serializers
from .models import Event, EventGuest


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'public_id',
            'title',
            'description',
            'start_datetime',
            'upload_expiry',
            'view_permission',
            'upload_permission',
            'require_approval',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'public_id',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'title':{'required':True},
        }

class EventGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGuest
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']
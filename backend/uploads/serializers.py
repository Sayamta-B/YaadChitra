from rest_framework import serializers
from .models import Upload


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = [
            'id',
            'name',
            'file',
            'caption',
            'upload_type',
            'file_size',
            'is_approved',
            'is_deleted',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'name',
            'file_size',
            'is_approved',
            'is_deleted',
            'created_at',
        ]
from django.contrib import admin
from .models import Upload, UploadAnalysis


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'event',
        'uploaded_by',
        'upload_type',
        'file_size',
        'is_approved',
        'is_deleted',
        'created_at',
    )

    list_filter = (
        'upload_type',
        'is_approved',
        'is_deleted',
        'created_at',
    )

    search_fields = (
        'name',
        'caption',
        'event__title',
        'uploaded_by__name',
    )

    readonly_fields = (
        'file_size',
        'created_at',
        'updated_at',
    )

    list_editable = (
        'is_approved',
        'is_deleted',
    )

    ordering = ('-created_at',)


@admin.register(UploadAnalysis)
class UploadAnalysisAdmin(admin.ModelAdmin):
    list_display = (
        'upload',
        'analysis_type',
        'status',
        'created_at',
    )

    list_filter = (
        'analysis_type',
        'status',
        'created_at',
    )

    search_fields = (
        'upload__name',
        'upload__event__title',
    )

    readonly_fields = (
        'created_at',
    )

    ordering = ('-created_at',)
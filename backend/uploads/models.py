from django.db import models
from django.conf import settings

class Upload(models.Model):
    class UploadType(models.TextChoices):
        IMAGE = "image", "Image"
        VIDEO = "video", "Video"
        OTHER = "other", "Other"

    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='uploads')
    uploaded_by = models.ForeignKey('events.EventGuest', on_delete=models.SET_NULL, null=True, blank=True, related_name='uploads')
    
    caption = models.TextField(blank=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%Y/%m/')

    upload_type = models.CharField(max_length=20, choices=UploadType.choices, default=UploadType.OTHER)
    file_size = models.PositiveIntegerField()

    is_approved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UploadAnalysis(models.Model):
    class  AnalysisType(models.TextChoices):
        BLUR = "blur", "Blur Detection"
        DUPLICATE = "duplicate", "Duplicate Detection"

    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name='analysis')
    analysis_type = models.CharField(max_length=20, choices=AnalysisType.choices)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')

    result = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.analysis_type} analysis for {self.upload.name}"

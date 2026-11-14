from django.urls import path
from .views import GuestUploadView, EventUploadListView, UploadDetailView

urlpatterns = [
    path('events/<str:public_id>/', GuestUploadView.as_view(), name='guest-upload'),
    path('events/<str:public_id>/gallery/', EventUploadListView.as_view(), name='event-gallery'),
    path('events/<str:public_id>/gallery/<int:pk>/', UploadDetailView.as_view(), name='upload-detail'),
]
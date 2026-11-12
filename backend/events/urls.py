from django.urls import path
from .views import EventListCreateView, EventDetailView

urlpatterns=[
    path('', EventListCreateView.as_view(), name='event-list-create'),
    path('<str:public_id>/', EventDetailView.as_view(), name='event-detail')
]
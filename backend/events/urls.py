from django.urls import path
from .views import EventListCreateView, EventDetailView, PublicEventDetailView, PublicEventListView

urlpatterns=[
    path('', EventListCreateView.as_view(), name='event-list-create'),

    path('public/', PublicEventListView.as_view(), name='public-event-list'),

    path('<str:public_id>/', EventDetailView.as_view(), name='event-detail'),
    path('public/<str:public_id>/', PublicEventDetailView.as_view(), name='public-event-detail'),
]
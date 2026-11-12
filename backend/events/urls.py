from django.urls import path
from .views import EventListCreateView, EventDetailView, PublicEventDetailView, PublicEventListView, GuestRegistrationView, EventGuestListView

urlpatterns = [
    path('', EventListCreateView.as_view(), name='event-list-create'),

    path('public/', PublicEventListView.as_view(), name='public-event-list'),
    path('public/<str:public_id>/', PublicEventDetailView.as_view(), name='public-event-detail'),

    path('<str:public_id>/guests/', GuestRegistrationView.as_view(), name='guest-registration'),
    path('<str:public_id>/guests/list/', EventGuestListView.as_view(), name='event-guest-list'),

    path('<str:public_id>/', EventDetailView.as_view(), name='event-detail'),
]
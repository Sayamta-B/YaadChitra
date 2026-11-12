from django.urls import path
from .views import RegisterView, LoginView, RefreshTokenView, LogoutView, ProfileView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('account/profile/', ProfileView.as_view(), name='profile'),
    path('account/profile/password/', ChangePasswordView.as_view(), name='change-password'),
]
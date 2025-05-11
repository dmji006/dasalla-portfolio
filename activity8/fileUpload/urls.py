from django.urls import path
from .views import UserRegistrationView, user_login, user_profile

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", user_login, name="login"),
    path("profile/", user_profile, name="profile"),
]

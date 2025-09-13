from django.urls import path
from apps.authentication.login.views import LoginView

urlpatterns = [
    path("", LoginView.as_view(), name="auth-login"),
]

from django.urls import path
from apps.authentication.forgot_password.views import ForgotPassView

urlpatterns = [
    path("", ForgotPassView.as_view(), name="auth-forgot-password"),
]

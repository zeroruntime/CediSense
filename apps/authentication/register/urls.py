from django.urls import path
from apps.authentication.register.views import RegisterView

urlpatterns = [
    path("", RegisterView.as_view(), name="auth-register"),
]

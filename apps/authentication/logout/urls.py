from django.urls import path
from apps.authentication.logout.views import logout_view

urlpatterns = [
    path("", logout_view, name="auth-logout"),
]

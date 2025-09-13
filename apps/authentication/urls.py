from django.urls import path, include

urlpatterns = [
    path("auth/login/", include("apps.authentication.login.urls")),
    path("auth/register/", include("apps.authentication.register.urls")),
    path("auth/forgot-pass/", include("apps.authentication.forgot_password.urls")),
    path("auth/logout/", include("apps.authentication.logout.urls")),

]

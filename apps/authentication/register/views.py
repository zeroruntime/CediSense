from apps.authentication.views import AuthView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.authentication.models import *


class RegisterView(AuthView):
    template_name = "register.html"

    def post(self, request, *args, **kwargs):
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if (
            User.objects.filter(username=username).exists()
            and User.objects.filter(email=email).exists()
        ):
            messages.info(request, "Username and email already taken!")
            return redirect("/auth/register/")

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already taken!")
            return redirect("/auth/register/")

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken!")
            return redirect("/auth/register/")

        first_name, last_name = self.process_full_name(full_name)
        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully!")
        return redirect("/auth/login/")

    def process_full_name(self, full_name):
        parts = full_name.strip().split()
        first_name = parts[0] if parts else ""
        last_name = " ".join(parts[1:]) if len(parts) > 1 else ""
        return first_name, last_name

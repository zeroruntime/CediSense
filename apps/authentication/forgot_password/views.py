from apps.authentication.views import AuthView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.authentication.models import *



class ForgotPassView(AuthView):
    template_name = "forgot_password.html"  # Login template

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Username or Password")
            return redirect("/auth/login/")

        login(request, user)
        return redirect("/")

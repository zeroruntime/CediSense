from django.views.generic import TemplateView
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to auth/urls.py file for more pages.
"""


class AuthView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Update the context
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )

        return context


# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, "Invalid Username")
            return redirect("/auth/login/")

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect("/auth/login/")
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect("/")

    # Render the login page template (GET request)
    return render(request, "auth_login_basic.html")


# Define a view function for the registration page
def register_page(request):

    def process_full_name(full_name):
        # Split the name by spaces
        parts = full_name.strip().split()

        # Handle cases where only one name is provided
        first_name = parts[0] if parts else ""
        last_name = " ".join(parts[1:]) if len(parts) > 1 else ""

        return first_name, last_name

    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if username is taken
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken!")
            return redirect("/auth/register/")

        # Check if email is taken
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already taken!")
            return redirect("/auth/register/")

        # Create a new User object with the provided information
        first_name, last_name = process_full_name(full_name)
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password  # create_user handles password hashing
        )
        user.save()

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect("/auth/login/")

    # Render the registration page template (GET request)
    return render(request, "auth_register_basic.html")

def forgot_pass (request):
    return render(request, "auth_forgot_password_basic.html")
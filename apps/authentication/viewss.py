from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from web_project.template_helpers.theme import TemplateHelper

class AuthView(View):
    registration_template = "auth_register_basic.html"
    login_template = "auth_login_basic.html"

    def get(self, request):
        # Determine which template to render based on request path
        template = (
            self.registration_template if "register" in request.path else self.login_template
        )
        
        # Render with layout context
        context = self.get_layout_context()
        return render(request, template, context)

    def post(self, request):
        if "register" in request.POST:
            return self.handle_registration(request)
        elif "login" in request.POST:
            return self.handle_login(request)

        messages.error(request, "Invalid form submission.")
        return redirect("/")

    def handle_registration(self, request):
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("/auth/register/")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken!")
            return redirect("/auth/register/")

        first_name, last_name = self.process_full_name(full_name)

        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully!")
        return redirect("/auth/login/")

    def handle_login(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Username or Password")
            return redirect("/auth/login/")

        login(request, user)
        return redirect("/")

    def process_full_name(self, full_name):
        parts = full_name.strip().split()
        first_name = parts[0] if parts else ""
        last_name = " ".join(parts[1:]) if len(parts) > 1 else ""
        return first_name, last_name
    
    def logout(request):
        logout(request)
        return redirect("/auth/login/")

    def get_layout_context(self):
        # Manually include layout context by calling TemplateLayout or similar utilities
        context = {}
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
                # Add any other necessary layout-specific context here
            }
        )
        return context

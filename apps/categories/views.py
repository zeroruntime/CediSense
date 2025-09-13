from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from apps.categories.forms import CategoryForm
from web_project import TemplateLayout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.dashboards.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages



"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to categories/urls.py file for more pages.
"""

@method_decorator(login_required, name='dispatch')
class CategoriesView(TemplateView):
    template_name = 'categories-page.html'

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['categories'] = Category.objects.filter(user=self.request.user)
        context['form'] = CategoryForm()
        return context

    def post(self, request, *args, **kwargs):
        if 'add_category' in request.POST:
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=False)
                category.user = request.user
                category.save()
                messages.success(request, 'Category added successfully!')
            else:
                messages.error(request, 'Error adding category. Please check the form.')

        elif 'edit_category' in request.POST:
            category_id = request.POST.get('category_id')
            try:
                category = Category.objects.get(pk=category_id, user=request.user)
                form = CategoryForm(request.POST, instance=category)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Category updated successfully!')
                else:
                    messages.error(request, 'Error updating category. Please check the form.')
            except Category.DoesNotExist:
                messages.error(request, 'Category not found.')

        elif 'delete_category' in request.POST:
            category_id = request.POST.get('category_id')
            try:
                category = Category.objects.get(pk=category_id, user=request.user)
                category.delete()
                messages.success(request, 'Category deleted successfully!')
            except Category.DoesNotExist:
                messages.error(request, 'Category not found.')

        return redirect('categories')
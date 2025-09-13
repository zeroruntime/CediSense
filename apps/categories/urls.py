from django.urls import path
from .views import CategoriesView



urlpatterns = [
    path(
        "categories/",
        CategoriesView.as_view(template_name="categories-page.html"),
        name="categories",
    )
]

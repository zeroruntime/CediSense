from django.urls import path, include
from .views import TransactionsView



urlpatterns = [
    path(
        "transactions/",
        TransactionsView.as_view(template_name="transactions.html"),
        name="transactions",
    ),
    path(
        "transactions/add-transactions/",
        include("apps.transactions.add_transactions.urls")
    ),
    path(
        "transactions/edit-transactions",
        include("apps.transactions.edit_transactions.urls")
    ),
    path(
        "transactions/delete-transactions/",
        include("apps.transactions.delete_transactions.urls")
    )
    
]

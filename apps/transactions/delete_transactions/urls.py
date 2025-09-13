from django.urls import path
from apps.transactions.delete_transactions.views import DeleteTransaction

urlpatterns = [
    path("", DeleteTransaction.as_view(), name="delete-transactions"),
]

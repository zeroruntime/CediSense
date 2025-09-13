from django.urls import path
from apps.transactions.edit_transactions.views import EditTransaction

urlpatterns = [
    path("", EditTransaction.as_view(), name="edit-transactions"),
]

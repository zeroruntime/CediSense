from django.urls import path
from apps.transactions.add_transactions.views import AddTransaction

urlpatterns = [
    path("", AddTransaction.as_view(), name="add-transactions"),
]

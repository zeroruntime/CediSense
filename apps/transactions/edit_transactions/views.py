from apps.transactions.models import Transaction
from apps.transactions.views import TransactionsView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from apps.dashboards.models import Income, Expense
from apps.transactions.forms import IncomeForm, ExpenseForm
from apps.categories.models import Category
from django.contrib.auth.models import User

class EditTransaction(TransactionsView):
    template_name = "edit_transactions.html"

    def get(self, request, *args, **kwargs):
        transaction_id = request.GET.get('transaction_id')
        context = self.get_context_data()

        try:
            # Try to get either Income or Expense
            try:
                transaction = Income.objects.get(id=transaction_id, user=request.user)
            except Income.DoesNotExist:
                transaction = Expense.objects.get(id=transaction_id, user=request.user)
            
            context["transaction"] = transaction
            return render(request, self.template_name, context)
            
        except (Income.DoesNotExist, Expense.DoesNotExist):
            messages.error(request, "Transaction not found.")
            return redirect("transactions")

    def post(self, request, *args, **kwargs):
        transaction_id = request.POST.get('transaction_id')
        try:
            # Try to get either Income or Expense
            try:
                transaction = Income.objects.get(id=transaction_id, user=request.user)
            except Income.DoesNotExist:
                transaction = Expense.objects.get(id=transaction_id, user=request.user)
            
            category = get_object_or_404(Category, id=request.POST.get('category'))
            
            # Update transaction
            transaction.category = category
            transaction.amount = request.POST.get('amount')
            transaction.date = request.POST.get('date')
            transaction.description = request.POST.get('description')
            transaction.save()
            
            messages.success(request, "Transaction updated successfully.")
            return redirect("transactions")
            
        except Exception as e:
            messages.error(request, f"Error updating transaction: {str(e)}")
            return redirect("transactions")
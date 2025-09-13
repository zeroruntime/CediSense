from apps.transactions.views import TransactionsView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from apps.dashboards.models import Income, Expense
from apps.transactions.forms import IncomeForm, ExpenseForm
from apps.categories.models import Category
from django.contrib.auth.models import User

class DeleteTransaction(TransactionsView):
    template_name = "delete_transactions.html"

    def get(self, request, *args, **kwargs):
        transaction_id = request.GET.get('transaction_id')

        try:
            # Try to get either Income or Expense
            try:
                transaction = Income.objects.get(id=transaction_id, user=request.user)
            except Income.DoesNotExist:
                transaction = Expense.objects.get(id=transaction_id, user=request.user)
            
            context = self.get_context_data()
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
            
            transaction.delete()
            messages.success(request, "Transaction deleted successfully.")
            
        except (Income.DoesNotExist, Expense.DoesNotExist):
            messages.error(request, "Transaction not found.")
        except Exception as e:
            messages.error(request, f"Error deleting transaction: {str(e)}")
            
        return redirect("transactions")

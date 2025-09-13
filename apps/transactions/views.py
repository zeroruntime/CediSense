from django.shortcuts import redirect
from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.dashboards.models import Income, Expense
from django.contrib.auth.decorators import login_required
from apps.categories.models import Category
from .models import Transaction
from django.db.models import Sum


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to transactions/urls.py file for more pages.
"""

@method_decorator(login_required, name='dispatch')
class TransactionsView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        
        transactions = (
            Income.objects.filter(user=self.request.user)
            .union(Expense.objects.filter(user=self.request.user))
            .order_by("-date")
        )
        
        categories = Category.objects.all()
        expense_categories = Category.objects.filter(type="Expense")
        income_categories = Category.objects.filter(type="Income")
        total_income = Income.objects.filter(user=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0
        total_expenses = Expense.objects.filter(user=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0
        balance = total_income - total_expenses
        
        context.update({
            'transactions' : transactions,
            'expense_categories' : expense_categories,
            'income_categories' : income_categories,
            'categories' : categories,
            'total_income' : total_income,
            'total_expenses' : total_expenses,
            'balance' : balance
        })

        return context


    # def income_list(self, request):
    #     incomes = Income.objects.filter(user=request.user)
        
    
    
    # def expense_list(self, request):
    #     expenses = Expense.objects.filter(user=request.user)
    

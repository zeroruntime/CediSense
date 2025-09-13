from apps.transactions.views import TransactionsView
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.dashboards.models import Income, Expense
from apps.transactions.forms import IncomeForm, ExpenseForm
from apps.categories.models import Category
from django.contrib.auth.models import User

class AddTransaction(TransactionsView):
    template_name = "add_transactions.html"

    def get(self, request, *args, **kwargs):
        income_categories = Category.objects.filter(type="Income")
        expense_categories = Category.objects.filter(type="Expense")

        transactions = (
            Income.objects.filter(user=request.user)
            .union(Expense.objects.filter(user=request.user))
            .order_by("-date")
        )

        return render(
            request,
            self.template_name,
            {
                "income_categories": income_categories,
                "expense_categories": expense_categories,
                "transactions": transactions,
            },
        )

    def post(self, request, *args, **kwargs):
        if 'income' in request.POST:
            try:
                # Get data from the POST request
                category_id = request.POST.get('category')
                amount = request.POST.get('amount')
                date = request.POST.get('date')
                description = request.POST.get('description')

                # Get category instance
                category = Category.objects.get(id=category_id, type="Income")

                # Create new Income instance
                Income.objects.create(
                    user=request.user,
                    category=category,
                    amount=amount,
                    date=date,
                    description=description,
                )

                messages.success(request, 'Income added successfully!')
                return redirect('transactions')

            except Category.DoesNotExist:
                messages.error(request, 'Invalid category selected.')
            except Exception as e:
                messages.error(request, f'Error adding income: {str(e)}')

        elif 'expense' in request.POST:
            try:
                # Get data from the POST request
                category_id = request.POST.get('category')
                amount = request.POST.get('amount')
                date = request.POST.get('date')
                description = request.POST.get('description')  

                # Get category instance
                category = Category.objects.get(id=category_id, type="Expense")

                # Create new Expense instance
                Expense.objects.create(
                    user=request.user,
                    category=category,
                    amount=amount,
                    date=date,
                    description=description
                )

                messages.success(request, 'Expense added successfully!')
                return redirect('transactions')

            except Category.DoesNotExist:
                messages.error(request, 'Invalid category selected.')
            except Exception as e:
                messages.error(request, f'Error adding expense: {str(e)}')

        return redirect('transactions')

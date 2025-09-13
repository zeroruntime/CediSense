# from urllib import request
from calendar import month_name
from datetime import date, datetime, timedelta
from decimal import Decimal
import json
from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Income, Expense
from apps.transactions.models import Transaction
from django.db.models import Sum, Q
from django.db.models.functions import TruncWeek


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""


@method_decorator(login_required, name="dispatch")
class DashboardsView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        first_name = self.request.user.first_name

        # Total Money
        total_income = (Income.objects.filter(user=self.request.user).aggregate(Sum("amount"))["amount__sum"]or 0)
        total_expenses = (Expense.objects.filter(user=self.request.user).aggregate(Sum("amount"))["amount__sum"]or 0)

        # Week Calculation
        current_week_start = date.today() - timedelta(days=date.today().weekday())

        income_this_week = (Income.objects.filter(user=self.request.user).annotate(week_start=TruncWeek("date")).filter(week_start=current_week_start).aggregate(income_total=Sum("amount")))

        expense_this_week = (Expense.objects.filter(user=self.request.user).annotate(week_start=TruncWeek("date")).filter(week_start=current_week_start).aggregate(expense_total=Sum("amount")))

        # Recent Transactions
        income_transactions = Income.objects.filter(user=self.request.user).values(
            "amount", "category__type", "category__name", "date", "description"
        )
        expense_transactions = Expense.objects.filter(user=self.request.user).values(
            "amount", "category__type", "category__name", "date", "description"
        )

        last_10_transactions = income_transactions.union(expense_transactions).order_by(
            "-date"
        )[:10]

        # Calculate balance
        balance = total_income - total_expenses

        # Monthly breakdown (for charts)
        income_by_month = (
            Income.objects.filter(user=self.request.user)
            .values("date__month")
            .annotate(total=Sum("amount"))
            .order_by("date__month")
        )
        expense_by_month = (
            Expense.objects.filter(user=self.request.user)
            .values("date__month")
            .annotate(total=Sum("amount"))
            .order_by("date__month")
        )

        income_by_month_named = [
            {"month": month_name[item["date__month"]], "total": item["total"]}
            for item in income_by_month
        ]
        expense_by_month_named = [
            {"month": month_name[item["date__month"]], "total": item["total"]}
            for item in expense_by_month
        ]

        # Categories Usage (For Charts)
        income_cat_data = (
            Income.objects.filter(user=self.request.user)
            .values("category__name")
            .annotate(total_amount=Sum("amount"))
            .order_by("-total_amount")
        )

        expense_cat_data = (
            Expense.objects.filter(user=self.request.user)
            .values("category__name")
            .annotate(total_amount=Sum("amount"))
            .order_by("-total_amount")
        )
        # Convert to the format needed for charts
        income_cat_list = [
            {
                'category': item['category__name'] or 'Uncategorized',
                'amount': float(item['total_amount'])
            }
            for item in income_cat_data
        ]

        expense_cat_list = [
            {
                'category': item['category__name'] or 'Uncategorized',
                'amount': float(item['total_amount'])
            }
            for item in expense_cat_data
        ]

        context.update(
            {
                "first_name": first_name,
                "total_income": total_income,
                "total_expenses": total_expenses,
                "balance": balance,
                "income_by_month": income_by_month,  # Income totals per month
                "expense_by_month": expense_by_month,  # Expense totals per month
                "income_by_month_named": income_by_month_named,
                "expense_by_month_named": expense_by_month_named,
                "income_this_week": income_this_week["income_total"] or 0,
                "expense_this_week": expense_this_week["expense_total"] or 0,
                "last_10_transactions": last_10_transactions,
                "income_cat_list" : income_cat_list,
                "expense_cat_list" : expense_cat_list
            }
        )

        return context

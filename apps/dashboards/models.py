from django.db import models
from django.contrib.auth.models import User
from apps.categories.models import Category
# Create your models here.


# class Category(models.Model):
#     CATEGORY_TYPES = [
#         ('income', 'Income'),
#         ('expense', 'Expense')
#     ]
    
#     name = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category_type = models.CharField(max_length=7, choices=CATEGORY_TYPES, null=True, blank=True)


#     def __str__(self):
#         return f"{self.name} ({self.get_category_type_display()})"

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, limit_choices_to={'type': 'Income'})
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.amount} - {self.category}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, limit_choices_to={'type': 'Expense'})
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.amount} - {self.category}"

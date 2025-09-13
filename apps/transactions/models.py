
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from apps.categories.models import Category

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    @property
    def type(self):
        # Derive type directly from the category’s type field
        return self.category.type if self.category else None

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount} GHS"
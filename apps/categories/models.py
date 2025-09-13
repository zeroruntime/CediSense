
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    CATEGORY_TYPES = [
        ('Expense', 'Expense'),
        ('Income', 'Income'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=CATEGORY_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  


    def __str__(self):
        return f"{self.name} ({self.type})"
    
    class Meta:
        verbose_name_plural = "Categories"

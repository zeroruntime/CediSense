from django import forms
from apps.categories.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text','class': 'form-control'}) ,
            'type': forms.Select(attrs={'class': 'form-select'}),
        }
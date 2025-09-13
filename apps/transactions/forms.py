from django import forms
from apps.dashboards.models import Income, Expense

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'category', 'date', 'description']
        widgets = {
            'amount' : forms.TextInput(attrs={'type':'number', 'class' : 'form-control', 'id' : 'amount', 'name' : 'amount', 'placeholder' : '0.00'}),
            'category' : forms.Select(attrs={ 'class' : 'form-select', 'id' : 'category', 'name' : 'category'}),
            'date' : forms.TextInput(attrs={'type':'date', 'class' : 'form-control', 'id' : 'date', 'name' : 'date'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control', 'id' : 'description', 'name' : 'description', 'rows' : '1', 'placeholder' : 'Add a note...'}),
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'date', 'description']
        widgets = {
            'amount' : forms.TextInput(attrs={'type':'number', 'class' : 'form-control', 'id' : 'amount', 'name' : 'amount', 'placeholder' : '0.00'}),
            'category' : forms.Select(attrs={ 'class' : 'form-select', 'id' : 'category', 'name' : 'category'}),
            'date' : forms.TextInput(attrs={'type':'date', 'class' : 'form-control', 'id' : 'date', 'name' : 'date'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control', 'id' : 'description', 'name' : 'description', 'rows' : '1', 'placeholder' : 'Add a note...'}),
        }
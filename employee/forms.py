from django import forms
from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee

        fields = ('nom', 'prenom', 'email', 'adress')

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom'}),
            'adress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adress'}),
        }
# forms.py
from django import forms
from .models import *

class SettlementForm(forms.ModelForm):
    class Meta:
        model = Settlement
        fields = [
            'date', 
            'washing', 
            'parking', 
            'income', 
            'news', 
            'expenses', 
            'remarks', 
            'image'
        ]
        labels = {
            'date': 'Fecha',
            'washing': 'Lavado',
            'parking': 'Estacionamiento',
            'income': 'Ingresos',
            'news': 'Novedades',
            'expenses': 'Gastos',
            'remarks': 'Observaciones',
            'image': 'Imagen',
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'washing': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'parking': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'news': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'expenses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe alguna observación'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class SettlementCenterForm(forms.ModelForm):
    class Meta:
        model = SettlementCentro
        fields = [
            'date', 
            'washing', 
            'parking', 
            'income', 
            'news', 
            'expenses', 
            'remarks', 
            'image'
        ]
        labels = {
            'date': 'Fecha',
            'washing': 'Lavado',
            'parking': 'Estacionamiento',
            'income': 'Ingresos',
            'news': 'Novedades',
            'expenses': 'Gastos',
            'remarks': 'Observaciones',
            'image': 'Imagen',
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'washing': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'parking': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'news': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'expenses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe alguna observación'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class SettlementJogalForm(forms.ModelForm):
    class Meta:
        model = SettlementJogal
        fields = [
            'date', 
            'washing', 
            'parking', 
            'income', 
            'news', 
            'expenses', 
            'remarks', 
            'image'
        ]
        labels = {
            'date': 'Fecha',
            'washing': 'Lavado',
            'parking': 'Estacionamiento',
            'income': 'Ingresos',
            'news': 'Novedades',
            'expenses': 'Gastos',
            'remarks': 'Observaciones',
            'image': 'Imagen',
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'washing': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'parking': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'news': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'expenses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe alguna observación'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

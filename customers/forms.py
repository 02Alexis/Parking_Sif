# forms.py
from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'vehicle', 'license_plate', 'price', 'payment_day']
        labels = {
            'name' : 'Nombre',
            'phone': 'Telefono',
            'vehicle': 'Vehiculo',
            'license_plate' : 'Placa',
            'price' : 'Precio',
            'payment_day' : 'Día de Pago',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_day': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CustomerCenterForm(forms.ModelForm):
    class Meta:
        model = CustomerCentro
        fields = ['name', 'phone', 'vehicle', 'license_plate', 'price', 'payment_day']
        labels = {
            'name' : 'Nombre',
            'phone': 'Telefono',
            'vehicle': 'Vehiculo',
            'license_plate' : 'Placa',
            'price' : 'Precio',
            'payment_day' : 'Día de Pago',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_day': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CustomerJogalForm(forms.ModelForm):
    class Meta:
        model = CustomerJogal
        fields = ['name', 'phone', 'vehicle', 'license_plate', 'price', 'payment_day']
        labels = {
            'name' : 'Nombre',
            'phone': 'Telefono',
            'vehicle': 'Vehiculo',
            'license_plate' : 'Placa',
            'price' : 'Precio',
            'payment_day' : 'Día de Pago',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_day': forms.NumberInput(attrs={'class': 'form-control'}),
        }

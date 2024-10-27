from django import forms
from .models import Invoice, MoreInfo
from django.forms import inlineformset_factory


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'date',
            'customer_name',
            'phone',
            'vehicle',
            'license_plate',
            'address',
            'document_type',
            'number',
        ]
        labels = {
            'date': 'Fecha de Emisión',
            'customer_name': 'Nombre del Cliente',
            'phone': 'Teléfono',
            'vehicle': 'Tipo de Vehículo',
            'license_plate': 'Placa del Vehículo',
            'address': 'Dirección',
            'document_type': 'Tipo de Documento',
            'number': 'Número de Documento',
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Cliente'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Placa del Vehículo'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'document_type': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Documento'}),
        }

class MoreInfoForm(forms.ModelForm):
    class Meta:
        model = MoreInfo
        fields = ['product', 'quantity', 'price']
        labels = {'product': 'Producto', 'quantity': 'Cantidad', 'price': 'Precio'}
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '15000'}),
        }

MoreInfoFormSet = inlineformset_factory(
    Invoice, MoreInfo, form=MoreInfoForm,
    extra=1, can_delete=True, can_delete_extra=True
)
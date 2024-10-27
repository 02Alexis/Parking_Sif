from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from .forms import *
from .models import *

# Create your views here.

# --------- vistas
def customers_hoyo(request):
    customers = Customer.objects.all().order_by('-id')

    ctx = {
        'customers': customers,
        'title': "Mensualidades",
        }
    return render(request, 'index/customer_hoyo.html', ctx)

def customers_center(request):
    customers_center = CustomerCentro.objects.all().order_by('-id')

    ctx = {
        'customers_center': customers_center,
        'title': "Mensualidades",
        }
    return render(request, 'index/customer_center.html', ctx)

def customers_jogal(request):
    customers_jogal = CustomerJogal.objects.all().order_by('-id')

    ctx = {
        'customers_jogal': customers_jogal,
        'title': "Mensualidades",
        }
    return render(request, 'index/customer_jogal.html', ctx)

# --------- funcion para crear
class CustomerCreateView(CreateView):
    template_name = 'form/create_customer_modal.html'
    model = Customer
    form_class = CustomerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Cliente'
        context['label'] = 'Crear'
        return context

    def get_success_url(self):
        return reverse('customer_hoyo')
    
class CustomerCreateCenterView(CreateView):
    template_name = 'form/create_customer_center_modal.html'
    model = CustomerCentro
    form_class = CustomerCenterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Cliente Centro'
        context['label'] = 'Crear'
        return context

    def get_success_url(self):
        return reverse('customer_center')
    
class CustomerCreateJogalView(CreateView):
    template_name = 'form/create_customer_jogal_modal.html'
    model = CustomerJogal
    form_class = CustomerJogalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Cliente Jogal'
        context['label'] = 'Crear'
        return context

    def get_success_url(self):
        return reverse('customer_jogal')

# --------- funcion para actualizar
class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'form/update_customer_modal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Cliente'
        context['label'] = 'Actualizar'
        return context

    def get_success_url(self):
        return reverse('customer_hoyo')
    
class CustomerCenterUpdateView(UpdateView):
    model = CustomerCentro
    form_class = CustomerCenterForm
    template_name = 'form/update_customer_center_modal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Cliente Centro'
        context['label'] = 'Actualizar'
        return context

    def get_success_url(self):
        return reverse('customer_center')
    
class CustomerJogalUpdateView(UpdateView):
    model = CustomerJogal
    form_class = CustomerJogalForm
    template_name = 'form/update_customer_jogal_modal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Cliente Jogal'
        context['label'] = 'Actualizar'
        return context

    def get_success_url(self):
        return reverse('customer_jogal')
    
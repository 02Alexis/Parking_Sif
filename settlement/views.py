from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
# --------- vistas
@login_required(login_url='login')
def home(request):
    return render(request, '404.html')

@login_required(login_url='login')
def index(request):
    settlements = Settlement.objects.all()

    ctx = {
        'settlements': settlements,
        'title': "Liquidaciones",
        }
    return render(request, 'index.html', ctx)

@login_required(login_url='login')
def parking_center(request):
    settlements_center = SettlementCentro.objects.all()

    ctx = {
        'settlements_center': settlements_center,
        'title': "Liquidaciones",
        }
    return render(request, 'settlements_center.html', ctx)

@login_required(login_url='login')
def parking_jogal(request):
    settlements_jogal = SettlementJogal.objects.all()

    ctx = {
        'settlements_jogal': settlements_jogal,
        'title': "Liquidaciones",
        }
    return render(request, 'settlements_jogal.html', ctx)

# --------- funcion para crear
class CreateSettlementView(CreateView):
    template_name = 'form/create_settlement_modal.html'
    model = Settlement
    form_class = SettlementForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Liquidación'
        context['label'] = 'Crear'
        return context

    def get_success_url(self):
        return reverse('parking')
    
class CreateSettlementCenterView(CreateView):
    template_name = 'form/create_settlement_center_modal.html'
    model = SettlementCentro
    form_class = SettlementCenterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Liquidación Centro'
        context['label'] = 'Crear'
        return context

    def get_success_url(self):
        return reverse('parking_center')
    
class CreateSettlementJogalView(CreateView):
    template_name = 'form/create_settlement_jogal_modal.html'
    model = SettlementJogal
    form_class = SettlementJogalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Liquidación Jogal'
        context['label'] = 'Crear'
        return context

    def get_success_url(self):
        return reverse('parking_jogal')
    
# --------- funcion para actualizar
class SettlementUpdateView(UpdateView):
    model = Settlement
    form_class = SettlementForm
    template_name = 'form/update_settlement_modal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Liquidación'
        context['label'] = 'Actualizar'
        return context

    def get_success_url(self):
        return reverse('parking')
    
class SettlementCenterUpdateView(UpdateView):
    model = SettlementCentro
    form_class = SettlementCenterForm
    template_name = 'form/update_settlement_center_modal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Liquidación Centro'
        context['label'] = 'Actualizar'
        return context

    def get_success_url(self):
        return reverse('parking_center')
    
class SettlementJogalUpdateView(UpdateView):
    model = SettlementJogal
    form_class = SettlementJogalForm
    template_name = 'form/update_settlement_jogal_modal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Liquidación Jogal'
        context['label'] = 'Actualizar'
        return context

    def get_success_url(self):
        return reverse('parking_jogal')
    
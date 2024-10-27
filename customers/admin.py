from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'vehicle', 'license_plate', 'price', 'payment_day')
    list_filter = ('vehicle', 'payment_day')
    search_fields = ('name', 'license_plate')

@admin.register(CustomerCentro)
class CustomerCentroAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'vehicle', 'license_plate', 'price', 'payment_day')
    list_filter = ('vehicle', 'payment_day')
    search_fields = ('name', 'license_plate')

@admin.register(CustomerJogal)
class CustomerJogalAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'vehicle', 'license_plate', 'price', 'payment_day')
    list_filter = ('vehicle', 'payment_day')
    search_fields = ('name', 'license_plate')
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Settlement)
class SettlementHoleAdmin(admin.ModelAdmin):
    list_display = ('date', 'washing', 'parking', 'income', 'expenses', 'settlement_amount', 'remarks')
    search_fields = ('date', 'remarks')

@admin.register(SettlementCentro)
class SettlementCentroAdmin(admin.ModelAdmin):
    list_display = ('date', 'washing', 'parking', 'income', 'news', 'expenses', 'settlement_amount', 'created_by')
    search_fields = ('date', 'created_by__username')

@admin.register(SettlementJogal)
class SettlementJogalAdmin(admin.ModelAdmin):
    list_display = ('date', 'washing', 'parking', 'income', 'news', 'expenses', 'settlement_amount', 'created_by')
    search_fields = ('date', 'created_by__username')
from django.urls import path
from . import views


urlpatterns = [
    path('parqueadero-hoyo/', views.index, name='parking'),
    path('parqueadero-centro/', views.parking_center, name='parking_center'),
    path('parqueadero-jogal/', views.parking_jogal, name='parking_jogal'),
    
    path('agregar-liquidacion/', views.CreateSettlementView.as_view(), name='add_parking'),
    path('agregar-liquidacion-centro/', views.CreateSettlementCenterView.as_view(), name='add_parking_center'),
    path('agregar-liquidacion-jogal/', views.CreateSettlementJogalView.as_view(), name='add_parking_jogal'),
    
    #--------------------- update
    path('liquidacion/<int:pk>/editar/', views.SettlementUpdateView.as_view(), name='update_parking'),
    path('liquidacion-centro/<int:pk>/editar/', views.SettlementCenterUpdateView.as_view(), name='update_parking_center'),
    path('liquidacion-jogal/<int:pk>/editar/', views.SettlementJogalUpdateView.as_view(), name='update_parking_jogal'),
]
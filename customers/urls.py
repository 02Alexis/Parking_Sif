from django.urls import path
from . import views


urlpatterns = [

    #--------------------- vista 
    path('parqueadero-hoyo/', views.customers_hoyo, name='customer_hoyo'),
    path('parqueadero-centro/', views.customers_center, name='customer_center'),
    path('parqueadero-jogal/', views.customers_jogal, name='customer_jogal'),

    #--------------------- create
    path('nuevo-cliente', views.CustomerCreateView.as_view(), name='create_customer'),
    path('nuevo-cliente-centro', views.CustomerCreateCenterView.as_view(), name='create_customer_center'),
    path('nuevo-cliente-jogal', views.CustomerCreateJogalView.as_view(), name='create_customer_jogal'),
    
    #--------------------- update
    path('cliente/<int:pk>/editar/', views.CustomerUpdateView.as_view(), name='update_customer'),
    path('cliente-centro/<int:pk>/editar/', views.CustomerCenterUpdateView.as_view(), name='update_customer_center'),
    path('cliente-jogal/<int:pk>/editar/', views.CustomerJogalUpdateView.as_view(), name='update_customer_jogal'),
    
]
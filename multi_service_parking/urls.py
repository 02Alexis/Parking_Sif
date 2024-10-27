from django.contrib import admin
from django.urls import path
from django.urls import include
from settlement import views
from multi_service_parking import views as login


urlpatterns = [
    path('', views.home, name='home'),
    path('users/login', login.login_view, name='login'),
    path('users/logout', login.logout_view, name='logout'),
    path('register/', login.register_view, name='register'),
    path('liquidacion/', include('settlement.urls')), # Ruta para la página de inicio
    path('mensualidad/', include('customers.urls')), # Ruta para la página de inicio
    path('factura-electronica/', include('invoice.urls')), # Ruta para la página de inicio
    path('admin/', admin.site.urls),
]

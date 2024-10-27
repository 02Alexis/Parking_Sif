from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    VEHICLE_CHOICES = [
        ('MOTO', 'Moto'),
        ('AUTOMOVIL', 'Automóvil'),
        ('TURBO', 'Turbo'),
        ('CAMIONETA', 'Camioneta'),
        ('CARRITO', 'Carrito'),
    ]
    name = models.CharField(max_length=100)  # Nombre del cliente
    phone = models.CharField(max_length=15)  # Teléfono del cliente
    vehicle = models.CharField(max_length=10, choices=VEHICLE_CHOICES)  # Tipo de vehículo (por ejemplo, carro, moto)
    license_plate = models.CharField(max_length=10)  # Placa del vehículo
    price = models.DecimalField(max_digits=10, decimal_places=0)  # Precio mensual
    payment_day = models.PositiveIntegerField()  # Día de pago (por ejemplo, 1, 15, 30)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Usuario que creó el registro

    def __str__(self):
        return f"{self.name} - {self.license_plate}"
    
class CustomerCentro(models.Model):
    VEHICLE_CHOICES = [
        ('MOTO', 'Moto'),
        ('AUTOMOVIL', 'Automóvil'),
        ('TURBO', 'Turbo'),
        ('CAMIONETA', 'Camioneta'),
        ('CARRITO', 'Carrito'),
    ]
    name = models.CharField(max_length=100)  # Nombre del cliente
    phone = models.CharField(max_length=15)  # Teléfono del cliente
    vehicle = models.CharField(max_length=10, choices=VEHICLE_CHOICES)  # Tipo de vehículo (por ejemplo, carro, moto)
    license_plate = models.CharField(max_length=10)  # Placa del vehículo
    price = models.DecimalField(max_digits=10, decimal_places=0)  # Precio mensual
    payment_day = models.PositiveIntegerField()  # Día de pago (por ejemplo, 1, 15, 30)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Usuario que creó el registro

    def __str__(self):
        return f"{self.name} - {self.license_plate}"

class CustomerJogal(models.Model):
    VEHICLE_CHOICES = [
        ('MOTO', 'Moto'),
        ('AUTOMOVIL', 'Automóvil'),
        ('TURBO', 'Turbo'),
        ('CAMIONETA', 'Camioneta'),
        ('CARRITO', 'Carrito'),
    ]
    name = models.CharField(max_length=100)  # Nombre del cliente
    phone = models.CharField(max_length=15)  # Teléfono del cliente
    vehicle = models.CharField(max_length=10, choices=VEHICLE_CHOICES)  # Tipo de vehículo (por ejemplo, carro, moto)
    license_plate = models.CharField(max_length=10)  # Placa del vehículo
    price = models.DecimalField(max_digits=10, decimal_places=0)  # Precio mensual
    payment_day = models.PositiveIntegerField()  # Día de pago (por ejemplo, 1, 15, 30)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Usuario que creó el registro

    def __str__(self):
        return f"{self.name} - {self.license_plate}"

from django.db import models
from django.contrib.auth.models import User

class Invoice(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('CEDULA', 'Cédula'),
        ('NIT', 'NIT'),
    ]
    
    VEHICLE_CHOICES = [
        ('MOTO', 'Moto'),
        ('AUTOMOVIL', 'Automóvil'),
        ('TURBO', 'Turbo'),
        ('CAMIONETA', 'Camioneta'),
        ('CARRITO', 'Carrito'),
    ]
    
    date = models.DateField()  # Fecha de emisión de la factura
    customer_name = models.CharField(max_length=100)  # Nombre del cliente
    phone = models.CharField(max_length=15)  # Teléfono del cliente
    vehicle = models.CharField(max_length=50, choices=VEHICLE_CHOICES)  # Tipo de vehículo (opcional si no es cliente)
    license_plate = models.CharField(max_length=10, blank=True, null=True)  # Placa del vehículo (opcional si no es cliente)
    address = models.CharField(max_length=255, blank=True, null=True)  # Dirección del cliente (opcional si no es cliente)
    document_type = models.CharField(max_length=10, choices=DOCUMENT_TYPE_CHOICES, blank=True, null=True)  # Tipo de documento (opcional)
    number = models.CharField(max_length=20, blank=True, null=True)  # Número de cédula o NIT (opcional)
    email = models.EmailField()  # Correo electrónico del cliente para enviar la factura
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Usuario que creó la factura

    def __str__(self):
        return f"Invoice {self.id} - {self.customer_name} - {self.vehicle}"
    
class MoreInfo(models.Model):
    PRODUCT_CHOICES = [
        ('PARKING_OCCASIONAL', 'Parqueo Ocasional'),
        ('MONTHLY_PAYMENT', 'Mensualidad'),
        ('WASH', 'Lavado'),
    ]
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.CharField(max_length=20, choices=PRODUCT_CHOICES)  # Producto
    quantity = models.PositiveIntegerField()  # Cantidad de productos
    price = models.DecimalField(max_digits=10, decimal_places=0)  # Precio

    def total_price(self):
        return self.quantity * self.price  # Multiplica cantidad por precio unitario

    def __str__(self):
        return f"{self.product} - {self.quantity} x {self.price}"


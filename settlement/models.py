from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Settlement(models.Model):
    date = models.DateField()  # Obligatorio
    washing = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    parking = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    income = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    news = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    expenses = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    settlement_amount = models.DecimalField(max_digits=10, decimal_places=0, editable=False, default=0)
    remarks = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='settlements/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)

    def save(self, *args, **kwargs):
        # Calcular la liquidación antes de guardar
        self.settlement_amount = (self.washing + self.parking + self.income) - (self.news + self.expenses)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Liquidación del {self.date}"
    
class SettlementCentro(models.Model):
    date = models.DateField()  # Obligatorio
    washing = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    parking = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    income = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    news = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    expenses = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    settlement_amount = models.DecimalField(max_digits=10, decimal_places=0, editable=False, default=0)
    remarks = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='settlements_centro/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)

    def save(self, *args, **kwargs):
        # Calcular la liquidación antes de guardar
        self.settlement_amount = (self.washing + self.parking + self.income) - (self.news + self.expenses)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Liquidación del parqueadero Centro {self.date}"

class SettlementJogal(models.Model):
    date = models.DateField()  # Obligatorio
    washing = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    parking = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    income = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    news = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    expenses = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    settlement_amount = models.DecimalField(max_digits=10, decimal_places=0, editable=False, default=0)
    remarks = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='settlements_jogal/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)

    def save(self, *args, **kwargs):
        # Calcular la liquidación antes de guardar
        self.settlement_amount = (self.washing + self.parking + self.income) - (self.news + self.expenses)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Liquidación parqueadero Jogal {self.date}"
    
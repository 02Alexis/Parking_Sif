# Generated by Django 3.2 on 2024-08-29 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SettlementJogal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('washing', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('parking', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('income', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('news', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('expenses', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('settlement_amount', models.DecimalField(decimal_places=0, default=0, editable=False, max_digits=10)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='settlements_jogal/')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SettlementCentro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('washing', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('parking', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('income', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('news', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('expenses', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('settlement_amount', models.DecimalField(decimal_places=0, default=0, editable=False, max_digits=10)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='settlements_centro/')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('washing', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('parking', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('income', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('news', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('expenses', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('settlement_amount', models.DecimalField(decimal_places=0, default=0, editable=False, max_digits=10)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='settlements/')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

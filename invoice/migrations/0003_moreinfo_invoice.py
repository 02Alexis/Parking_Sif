# Generated by Django 3.2 on 2024-09-14 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20240914_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='moreinfo',
            name='invoice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice'),
            preserve_default=False,
        ),
    ]

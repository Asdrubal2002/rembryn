# Generated by Django 3.2.2 on 2022-12-02 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0002_alter_cotizacion_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='proyecto',
        ),
    ]

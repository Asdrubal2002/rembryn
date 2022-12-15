# Generated by Django 3.2.2 on 2022-12-09 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0002_auto_20221022_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignacion_material',
            name='material',
        ),
        migrations.AddField(
            model_name='asignacion_material',
            name='material',
            field=models.ManyToManyField(related_name='material', to='materiales.Material'),
        ),
    ]

# Generated by Django 3.2.2 on 2022-12-02 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20221202_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='identificacion',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

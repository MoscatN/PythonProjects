# Generated by Django 4.1.1 on 2022-09-25 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RHApp', '0011_experiencialaboral_createdby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencialaboral',
            name='Fecha_Desde',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='experiencialaboral',
            name='Fecha_Hasta',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RHApp', '0005_alter_candidatos_cedula_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='SalarioMensual',
            field=models.IntegerField(max_length=44, null=True),
        ),
    ]

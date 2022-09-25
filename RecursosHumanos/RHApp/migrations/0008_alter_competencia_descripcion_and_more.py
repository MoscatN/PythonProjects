# Generated by Django 4.1.1 on 2022-09-24 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RHApp', '0007_candidatos_salarioaspirado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competencia',
            name='Descripcion',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='experiencialaboral',
            name='Fecha_Desde',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='experiencialaboral',
            name='Fecha_Hasta',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='Idioma',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
# Generated by Django 4.1.1 on 2022-09-12 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RHApp', '0003_capacitaciones_competencia_experiencialaboral_puesto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idioma',
            name='Idioma',
            field=models.CharField(max_length=200),
        ),
    ]

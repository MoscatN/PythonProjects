# Generated by Django 4.1.1 on 2022-09-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RHApp', '0013_remove_candidatos_capacitacionesprincipales_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatos',
            name='CompetenciasPrincipales',
        ),
        migrations.AddField(
            model_name='candidatos',
            name='CompetenciasPrincipales',
            field=models.ManyToManyField(to='RHApp.competencia'),
        ),
    ]

# Generated by Django 4.1 on 2022-09-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RHApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Idioma', models.TextField(max_length=200)),
                ('Activo', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Competencias',
        ),
    ]

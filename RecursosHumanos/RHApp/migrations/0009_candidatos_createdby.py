# Generated by Django 4.1.1 on 2022-09-25 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RHApp', '0008_alter_competencia_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatos',
            name='createdBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-25 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RHApp', '0010_alter_candidatos_createdby'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencialaboral',
            name='createdBy',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

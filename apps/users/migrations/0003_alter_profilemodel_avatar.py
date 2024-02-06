# Generated by Django 5.0.1 on 2024-02-06 19:04

import core.services.file_service
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilemodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=core.services.file_service.FileService.upload_avatar),
        ),
    ]

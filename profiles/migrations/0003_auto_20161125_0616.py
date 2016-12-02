# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=profiles.models.avatar_path, verbose_name='profile picture'),
        ),
    ]

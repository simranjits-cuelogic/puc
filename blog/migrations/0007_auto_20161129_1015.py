# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20161129_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desription',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

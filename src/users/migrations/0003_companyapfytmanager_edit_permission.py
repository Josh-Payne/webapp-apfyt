# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170318_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyapfytmanager',
            name='edit_permission',
            field=models.BooleanField(default=False),
        ),
    ]

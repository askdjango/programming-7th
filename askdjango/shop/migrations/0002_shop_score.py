# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='score',
            field=models.SmallIntegerField(default=0),
        ),
    ]

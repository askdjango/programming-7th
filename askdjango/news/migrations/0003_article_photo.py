# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
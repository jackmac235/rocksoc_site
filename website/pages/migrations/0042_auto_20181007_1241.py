# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-07 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0041_image_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.TextField(blank=True, default=''),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-21 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0038_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='album',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.Album'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-19 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20180403_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='wus',
            field=models.BooleanField(default=False),
        ),
    ]
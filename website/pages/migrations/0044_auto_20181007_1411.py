# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-07 13:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0043_album_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album_category',
            options={'verbose_name_plural': 'Album_categories'},
        ),
    ]
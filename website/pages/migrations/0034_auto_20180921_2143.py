# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-21 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0033_auto_20180921_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orders_products',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orders_products',
            name='product',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='Orders_Products',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]

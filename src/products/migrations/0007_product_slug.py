# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-09 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='abc'),
            preserve_default=False,
        ),
    ]

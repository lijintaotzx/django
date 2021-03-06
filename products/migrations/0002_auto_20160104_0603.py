# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 05:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('MAL', 'Male'), ('FEM', 'Female'), ('NON', '')],
                                   default='NON', max_length=3),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 23:08
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160119_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='product',
            name='longitude',
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField('POINT=(0, 0)', srid=4326),
            preserve_default=False,
        ),
    ]

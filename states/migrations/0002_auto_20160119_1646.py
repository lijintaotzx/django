# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 15:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 19, 15, 46, 16, 827791, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 19, 15, 46, 23, 206237, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 09:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171023_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 24, 9, 56, 36, 541891, tzinfo=utc)),
        ),
    ]

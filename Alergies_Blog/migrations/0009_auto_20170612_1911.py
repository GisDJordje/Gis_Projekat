# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-06-12 17:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Alergies_Blog', '0008_auto_20170609_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 12, 17, 11, 44, 241373, tzinfo=utc)),
        ),
    ]
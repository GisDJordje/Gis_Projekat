# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-06-09 19:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Alergies_Blog', '0006_auto_20170609_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 9, 19, 30, 28, 545379, tzinfo=utc)),
        ),
    ]
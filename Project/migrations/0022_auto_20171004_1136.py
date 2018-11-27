# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 03:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0021_auto_20171004_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationfee',
            name='Date_in',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkoutticket',
            name='DateTime_out',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 11, 36, 52, 836816)),
        ),
        migrations.AlterField(
            model_name='reservationfee',
            name='DateTime_paid',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 11, 36, 52, 836816)),
        ),
        migrations.AlterField(
            model_name='reserveparking',
            name='DateTimeReservation',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 11, 36, 52, 836816)),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 22:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0014_auto_20171001_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutticket',
            name='DateTime_out',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 6, 34, 43, 71447)),
        ),
        migrations.AlterField(
            model_name='reservationfee',
            name='DateTime_paid',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 6, 34, 43, 71947)),
        ),
        migrations.AlterField(
            model_name='reserveparking',
            name='DateTimeReservation',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 6, 34, 43, 70945)),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20170127_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackerinfo',
            name='attendee_status',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.AttendeeStatus'),
            preserve_default=False,
        ),
    ]

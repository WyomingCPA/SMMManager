# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 12:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('VKApp', '0002_checkpublicpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='visible',
        ),
        migrations.AddField(
            model_name='parseritemgroups',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 8, 4, 12, 21, 49, 185000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]

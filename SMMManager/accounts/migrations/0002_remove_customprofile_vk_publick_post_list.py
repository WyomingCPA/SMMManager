# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 00:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customprofile',
            name='vk_publick_post_list',
        ),
    ]

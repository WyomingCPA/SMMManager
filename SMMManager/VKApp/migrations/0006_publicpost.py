# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 00:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('VKApp', '0005_remove_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_publick', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VKApp.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

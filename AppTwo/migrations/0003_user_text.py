# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-10-14 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0002_auto_20201013_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
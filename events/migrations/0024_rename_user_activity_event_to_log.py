# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 00:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_auto_20171003_0322'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserActivityEvent',
            new_name='UserActivityLog',
        ),
    ]
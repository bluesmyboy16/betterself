# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 08:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20170529_0204'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sleepeventlog',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='sleepeventlog',
            name='user',
        ),
        migrations.DeleteModel(
            name='SleepEventLog',
        ),
    ]
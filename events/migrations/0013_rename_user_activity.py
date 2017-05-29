# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-28 04:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_rename_duration_minutes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useractivityevent',
            old_name='activity',
            new_name='user_activity',
        ),
        migrations.AlterUniqueTogether(
            name='useractivityevent',
            unique_together=set([('time', 'user', 'user_activity')]),
        ),
    ]
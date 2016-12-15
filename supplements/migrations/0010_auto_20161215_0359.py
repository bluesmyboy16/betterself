# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-15 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplements', '0009_auto_20161215_0357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredientcomposition',
            options={'ordering': ['user', 'ingredient__name'], 'verbose_name': 'Ingredient Composition', 'verbose_name_plural': 'Ingredient Compositions'},
        ),
        migrations.AlterModelOptions(
            name='supplement',
            options={'ordering': ['user', 'name'], 'verbose_name': 'Supplement', 'verbose_name_plural': 'Supplements'},
        ),
    ]

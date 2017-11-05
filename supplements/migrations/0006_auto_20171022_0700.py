# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplements', '0005_adjust_supplement_stack_to_include_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersupplementstackcomposition',
            name='stack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compositions', to='supplements.UserSupplementStack'),
        ),
    ]
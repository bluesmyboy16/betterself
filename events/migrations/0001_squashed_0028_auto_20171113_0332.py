# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 22:23
from __future__ import unicode_literals

import betterself.utils.date_utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    replaces = [('events', '0001_initial'), ('events', '0002_switch_to_decimal_field'), ('events', '0003_add_unique_constraints_of_time_and_supplement'), ('events', '0004_productive_models_creation'), ('events', '0005_null_true_for_productive_logs'), ('events', '0006_productive_log_ordering'), ('events', '0007_switch_day_to_date'), ('events', '0008_auto_20170205_0228'), ('events', '0009_supplementevent_duration'), ('events', '0010_auto_20170521_2251'), ('events', '0011_add_activity_events'), ('events', '0012_rename_duration_minutes'), ('events', '0013_rename_user_activity'), ('events', '0014_auto_20170529_0204'), ('events', '0015_auto_20170618_0832'), ('events', '0016_sleepactivitylog'), ('events', '0017_auto_20170618_1019'), ('events', '0018_auto_20170618_1021'), ('events', '0019_auto_20170626_2114'), ('events', '0020_useractivity_is_all_day_activity'), ('events', '0021_auto_20170905_0212'), ('events', '0022_supplement_reminder_additions'), ('events', '0023_auto_20171003_0322'), ('events', '0024_rename_user_activity_event_to_log'), ('events', '0025_sleep_activity_rename'), ('events', '0026_rename_productivity_event_to_log'), ('events', '0027_add_user_mood'), ('events', '0028_auto_20171113_0332')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('supplements', '0003_data_migrations_for_measurements'),
        ('supplements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SleepEventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('source', models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel')], max_length=50)),
                ('sleep_time_minutes', models.IntegerField()),
                ('day', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SupplementEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('source', models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel'), ('text_message', 'Text_Message')], default='web', max_length=50)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time', models.DateTimeField()),
                ('supplement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplements.Supplement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('duration_minutes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Supplement Events',
                'verbose_name': 'Supplement Event',
                'ordering': ['user', '-time'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='supplementevent',
            unique_together=set([('user', 'time', 'supplement')]),
        ),
        migrations.CreateModel(
            name='DailyProductivityLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('source', models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel')], max_length=50)),
                ('day', models.DateField()),
                ('very_productive_time_minutes', models.PositiveIntegerField(blank=True, null=True)),
                ('productive_time_minutes', models.PositiveIntegerField(blank=True, null=True)),
                ('neutral_time_minutes', models.PositiveIntegerField(blank=True, null=True)),
                ('distracting_time_minutes', models.PositiveIntegerField(blank=True, null=True)),
                ('very_distracting_time_minutes', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sleepeventlog',
            unique_together=set([('day', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='dailyproductivitylog',
            unique_together=set([('day', 'user')]),
        ),
        migrations.AlterModelOptions(
            name='dailyproductivitylog',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='dailyproductivitylog',
            old_name='day',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='sleepeventlog',
            old_name='day',
            new_name='date',
        ),
        migrations.AlterUniqueTogether(
            name='dailyproductivitylog',
            unique_together=set([('date', 'user')]),
        ),
        migrations.AlterField(
            model_name='sleepeventlog',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='sleepeventlog',
            unique_together=set([]),
        ),
        migrations.AlterModelOptions(
            name='dailyproductivitylog',
            options={'ordering': ['-date'], 'verbose_name': 'Daily Productivity Log', 'verbose_name_plural': 'Daily Productivity Logs'},
        ),
        migrations.AlterField(
            model_name='dailyproductivitylog',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('is_significant_activity', models.BooleanField(default=False)),
                ('is_negative_activity', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivityEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('source', models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel')], default='web', max_length=50)),
                ('duration_minutes', models.IntegerField(default=0)),
                ('time', models.DateTimeField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.UserActivity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='useractivityevent',
            unique_together=set([('time', 'user', 'activity')]),
        ),
        migrations.AlterUniqueTogether(
            name='useractivity',
            unique_together=set([('name', 'user')]),
        ),
        migrations.RenameField(
            model_name='useractivityevent',
            old_name='activity',
            new_name='user_activity',
        ),
        migrations.AlterUniqueTogether(
            name='useractivityevent',
            unique_together=set([('time', 'user', 'user_activity')]),
        ),
        migrations.AlterModelOptions(
            name='useractivityevent',
            options={'ordering': ['user', '-time']},
        ),
        migrations.RemoveField(
            model_name='sleepeventlog',
            name='user',
        ),
        migrations.DeleteModel(
            name='SleepEventLog',
        ),
        migrations.CreateModel(
            name='SleepLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('source', models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel'), ('text_message', 'Text_Message')], max_length=50)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sleep Activity Logs',
                'ordering': ['user', '-end_time'],
                'verbose_name': 'Sleep Activity Log',
            },
        ),
        migrations.AlterModelOptions(
            name='useractivity',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='useractivity',
            name='is_all_day_activity',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='SupplementReminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('reminder_time', models.TimeField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_sent_reminder_time', models.DateTimeField(null=True)),
                ('supplement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplements.Supplement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='supplementreminder',
            unique_together=set([('user', 'reminder_time', 'supplement')]),
        ),
        migrations.AlterModelOptions(
            name='supplementreminder',
            options={'verbose_name': 'Supplement Reminder', 'verbose_name_plural': 'Supplement Reminders'},
        ),
        migrations.AlterField(
            model_name='dailyproductivitylog',
            name='source',
            field=models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel'), ('text_message', 'Text_Message')], max_length=50),
        ),
        migrations.AlterField(
            model_name='supplementreminder',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='useractivityevent',
            name='source',
            field=models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel'), ('text_message', 'Text_Message')], default='web', max_length=50),
        ),
        migrations.RenameModel(
            old_name='UserActivityEvent',
            new_name='UserActivityLog',
        ),
        migrations.RenameModel(
            old_name='SupplementEvent',
            new_name='SupplementLog',
        ),
        migrations.CreateModel(
            name='UserMoodLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('time', models.DateTimeField()),
                ('value', models.PositiveSmallIntegerField()),
                ('notes', models.TextField(blank=True)),
                ('source', models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel'), ('text_message', 'Text_Message')], default='web', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Mood Logs',
                'verbose_name': 'Mood Log',
            },
        ),
        migrations.AlterUniqueTogether(
            name='usermoodlog',
            unique_together=set([('user', 'time')]),
        ),
        migrations.AlterModelOptions(
            name='usermoodlog',
            options={'ordering': ['user', '-time'], 'verbose_name': 'Mood Log', 'verbose_name_plural': 'Mood Logs'},
        ),
        migrations.AlterField(
            model_name='usermoodlog',
            name='time',
            field=models.DateTimeField(default=betterself.utils.date_utils.get_current_utc_time_and_tz),
        ),
    ]
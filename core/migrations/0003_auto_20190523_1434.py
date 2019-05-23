# Generated by Django 2.1.7 on 2019-05-23 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190523_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='removedrecurredschedule',
            name='rule',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='parentSchedule',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='recurrenceRule',
        ),
        migrations.AddField(
            model_name='profile',
            name='calendar',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Calendar'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='subtitle',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.RemoveField(
            model_name='event',
            name='calendarId',
        ),
        migrations.AddField(
            model_name='event',
            name='calendarId',
            field=models.ManyToManyField(related_name='schedules', related_query_name='schedule', to='core.Calendar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='RecurrenceRule',
        ),
        migrations.DeleteModel(
            name='RemovedRecurredSchedule',
        ),
    ]
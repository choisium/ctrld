# Generated by Django 2.1.7 on 2019-05-23 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190523_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='calendar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Calendar'),
        ),
    ]
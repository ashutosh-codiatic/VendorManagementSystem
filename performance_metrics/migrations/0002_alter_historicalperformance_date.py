# Generated by Django 4.2.9 on 2024-01-11 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance_metrics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 16, 59, 33, 989421)),
        ),
    ]
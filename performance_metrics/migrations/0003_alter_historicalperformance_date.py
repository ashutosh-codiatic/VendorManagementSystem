# Generated by Django 4.2.9 on 2024-01-11 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance_metrics', '0002_alter_historicalperformance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 17, 3, 37, 248039)),
        ),
    ]

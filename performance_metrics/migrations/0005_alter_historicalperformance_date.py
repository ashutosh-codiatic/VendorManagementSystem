# Generated by Django 4.2.9 on 2024-01-12 05:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('performance_metrics', '0004_alter_historicalperformance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

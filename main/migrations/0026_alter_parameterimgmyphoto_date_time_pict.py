# Generated by Django 5.0 on 2024-01-24 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_parameterimgmyphoto_date_time_pict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameterimgmyphoto',
            name='date_time_pict',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 18, 26, 46, 394167), max_length=16),
            preserve_default=False,
        ),
    ]
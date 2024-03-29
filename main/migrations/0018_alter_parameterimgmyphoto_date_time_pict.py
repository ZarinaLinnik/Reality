# Generated by Django 5.0 on 2024-01-23 14:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_parameterimgmyphoto_date_time_pict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameterimgmyphoto',
            name='date_time_pict',
            field=models.DateTimeField(validators=[django.core.validators.RegexValidator(code='invalid_date_time', message='Date and time format should be YYYY-MM-DD HH:MM:SS', regex='^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}$')]),
        ),
    ]

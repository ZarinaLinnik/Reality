# Generated by Django 5.0 on 2024-01-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_parameterimgmyphoto_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameterimgmyphoto',
            name='date_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='parameterimgmyphoto',
            name='date_time_pict',
            field=models.DateTimeField(default='02/20/2005 17:25'),
        ),
    ]
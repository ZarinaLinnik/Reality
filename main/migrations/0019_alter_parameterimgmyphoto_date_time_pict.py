# Generated by Django 5.0 on 2024-01-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_parameterimgmyphoto_date_time_pict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameterimgmyphoto',
            name='date_time_pict',
            field=models.DateTimeField(),
        ),
    ]
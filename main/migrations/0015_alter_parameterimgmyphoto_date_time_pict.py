# Generated by Django 5.0 on 2024-01-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_parameter1whoareyou_text0_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameterimgmyphoto',
            name='date_time_pict',
            field=models.DateTimeField(),
        ),
    ]
# Generated by Django 5.0 on 2023-12-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
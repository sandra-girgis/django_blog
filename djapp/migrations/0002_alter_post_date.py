# Generated by Django 4.0.2 on 2022-02-16 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

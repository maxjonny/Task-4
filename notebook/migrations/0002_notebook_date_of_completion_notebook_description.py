# Generated by Django 4.0.5 on 2022-07-01 11:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='date_of_completion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notebook',
            name='description',
            field=models.TextField(default=''),
        ),
    ]

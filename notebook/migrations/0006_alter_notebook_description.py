# Generated by Django 4.0.5 on 2022-07-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0005_alter_notebook_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
# Generated by Django 4.0.5 on 2022-07-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0004_alter_notebook_header_alter_notebook_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='status',
            field=models.IntegerField(choices=[(0, 'выполняется'), (1, 'выполнено')], default=0),
        ),
    ]

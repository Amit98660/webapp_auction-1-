# Generated by Django 4.2.2 on 2023-08-22 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 11, 6, 13, 499487)),
        ),
    ]

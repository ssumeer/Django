# Generated by Django 3.2 on 2021-10-24 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='when',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 24, 15, 52, 3, 104873)),
        ),
    ]

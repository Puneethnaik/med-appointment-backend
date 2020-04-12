# Generated by Django 2.2.9 on 2020-04-12 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_mobileclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 15, 1, 52, 232143, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 15, 2, 4, 7705, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

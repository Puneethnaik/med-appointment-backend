# Generated by Django 2.2.9 on 2020-04-09 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200407_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='worksfor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

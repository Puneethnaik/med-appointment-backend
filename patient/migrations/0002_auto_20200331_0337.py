# Generated by Django 2.2.9 on 2020-03-31 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
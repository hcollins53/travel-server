# Generated by Django 4.2.2 on 2023-06-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapi', '0002_trip_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='dates',
        ),
        migrations.AddField(
            model_name='trip',
            name='end_date',
            field=models.CharField(default='03/30/23', max_length=60),
        ),
        migrations.AddField(
            model_name='trip',
            name='start_date',
            field=models.CharField(default='03/23/23', max_length=60),
        ),
    ]

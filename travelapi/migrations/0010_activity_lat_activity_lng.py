# Generated by Django 4.2.2 on 2023-06-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapi', '0009_remove_activity_cost_remove_activity_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='lat',
            field=models.CharField(default='36.1627', max_length=30),
        ),
        migrations.AddField(
            model_name='activity',
            name='lng',
            field=models.CharField(default='86.7816', max_length=30),
        ),
    ]
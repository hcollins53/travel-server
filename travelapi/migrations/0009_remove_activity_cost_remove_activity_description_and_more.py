# Generated by Django 4.2.2 on 2023-06-09 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapi', '0008_rename_booking_link_activity_website_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='description',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='website',
        ),
        migrations.AddField(
            model_name='activity',
            name='place_id',
            field=models.CharField(default='link', max_length=100),
        ),
        migrations.AddField(
            model_name='activity',
            name='vicinity',
            field=models.CharField(default='somewhere', max_length=50),
        ),
    ]
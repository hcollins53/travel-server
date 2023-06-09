# Generated by Django 4.2.2 on 2023-06-16 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapi', '0017_hotel_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapi.budget')),
            ],
        ),
        migrations.AddField(
            model_name='budget',
            name='expenses',
            field=models.ManyToManyField(related_name='budgetSpending', to='travelapi.spending'),
        ),
        migrations.AddField(
            model_name='budget',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapi.trip'),
        ),
    ]

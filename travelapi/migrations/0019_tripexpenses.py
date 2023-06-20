# Generated by Django 4.2.2 on 2023-06-19 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapi', '0018_budget_spending_budget_expenses_budget_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapi.budget')),
                ('spending', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapi.spending')),
            ],
        ),
    ]
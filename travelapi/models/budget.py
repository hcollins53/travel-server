from django.db import models



class Budget(models.Model):
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE)
    amount = models.IntegerField()
    expenses = models.ManyToManyField("TripExpenses", related_name="budgetSpending")
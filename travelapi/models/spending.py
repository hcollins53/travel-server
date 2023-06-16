from django.db import models



class Spending(models.Model):
    expense = models.CharField(max_length=50)
    amount = models.IntegerField()
    budget = models.ForeignKey("Budget", on_delete=models.CASCADE)
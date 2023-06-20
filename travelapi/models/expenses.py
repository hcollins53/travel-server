from django.db import models



class TripExpenses(models.Model):
    budget = models.ForeignKey("Budget", on_delete=models.CASCADE)
    spending = models.ForeignKey("Spending", on_delete=models.CASCADE)

    @property
    def spending_amount(self):
        return f'{self.spending.amount}'
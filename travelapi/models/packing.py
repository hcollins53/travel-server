from django.db import models



class Packing(models.Model):
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    amount = models.IntegerField()
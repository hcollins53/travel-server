from django.db import models



class Activity(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    cost = models.CharField(max_length=20)
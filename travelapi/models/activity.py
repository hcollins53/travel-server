from django.db import models



class Activity(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    cost = models.CharField(max_length=20)
    description = models.CharField(max_length=500, default="An activity")
    booking_link = models.CharField(max_length=500, default="a link")
    picture = models.CharField(max_length=500, default="image link")
    minimum_duration = models.CharField(max_length=50, default="1hr")

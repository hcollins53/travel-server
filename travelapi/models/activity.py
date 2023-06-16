from django.db import models



class Activity(models.Model):
    name = models.CharField(max_length=500)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    place_id = models.CharField(max_length=100, default="link")
    rating = models.CharField(max_length=10, default="4")
    vicinity = models.CharField(max_length=100, default="somewhere")
    lat = models.FloatField(max_length=30, default=40.7128)
    lng = models.FloatField(max_length=30, default=74.0060)
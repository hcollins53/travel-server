from django.db import models



class Hotel(models.Model):
    name = models.CharField(max_length=100)
    place_id = models.CharField(max_length=100, default="link")
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    rating = models.CharField(max_length=10, default="4")
    vicinity = models.CharField(max_length=50, default="somewhere")
    lat = models.FloatField(max_length=30, default=40.7128)
    lng = models.FloatField(max_length=30, default=74.0060)
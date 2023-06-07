from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.CharField(max_length=60, default="03/23/23")
    end_date = models.CharField(max_length=60, default="03/30/23")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    locations = models.ManyToManyField("TripLocation", related_name="trip_places")
    details = models.ManyToManyField("ActivityItinerary", related_name='itinerary_details')
    

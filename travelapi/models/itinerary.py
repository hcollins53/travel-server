from django.db import models

class Itinerary(models.Model):
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE)
    details = models.ManyToManyField("ActivityItinerary", related_name='itinerary_details')

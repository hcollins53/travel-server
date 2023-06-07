from django.db import models


class TripLocation(models.Model):
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='trip_locations')
    location = models.ForeignKey("Location", on_delete=models.CASCADE, related_name='trip_locations')
    
    @property
    def location_name(self):
        return f'{self.location.name}'

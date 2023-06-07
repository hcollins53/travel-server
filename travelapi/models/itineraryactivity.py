from django.db import models

class ActivityItinerary(models.Model):
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='activity_itinerary')
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE, related_name='activity_itinerary')

    @property
    def location_name(self):
        return f'{self.location.name}'
    @property
    def activity_name(self):
        return f'{self.activity.name}'
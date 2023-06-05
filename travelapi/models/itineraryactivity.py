from django.db import models

class ActivityItinerary(models.Model):
    itinerary = models.ForeignKey("Itinerary", on_delete=models.CASCADE, related_name='activity_itinerary')
    day = models.ForeignKey("Day", on_delete=models.CASCADE)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE, related_name='activity_itinerary')
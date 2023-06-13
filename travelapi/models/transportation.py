from django.db import models



class Travel(models.Model):
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE)
    dep_date = models.CharField(max_length=20)
    transport_type = models.CharField(max_length=20)
    dep_time = models.CharField(max_length=20)
    arr_time = models.CharField(max_length=20)
    dep_location = models.ForeignKey("Location", on_delete=models.CASCADE, related_name="departures")
    arr_location = models.ForeignKey("Location", on_delete=models.CASCADE, related_name="arrivals")
    
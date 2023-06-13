from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.CharField(max_length=60, default="03/23/23")
    end_date = models.CharField(max_length=60, default="03/30/23")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    locations = models.ManyToManyField("TripLocation", related_name="trip_places")
    details = models.ManyToManyField("ActivityItinerary", related_name='itinerary_details')
    image = models.CharField(max_length=300, default="https://mail.google.com/mail/u/0?ui=2&ik=d893f429cf&attid=0.1.1&permmsgid=msg-f:1767541423958244148&th=1887918f6cd1bb34&view=fimg&fur=ip&sz=s0-l75-ft&attbid=ANGjdJ95c40vVKXqgO0e9LrAiKHqbAXDkCDO8-RdHTQ6fN-hUMhuBFv1aHRqSP4BmfGrN66PZx5jsJBtXR_yOmRKY9qiCLUKqJhZZNUFU0_Yd-oLu6BxxS3iy4sGWis&disp=emb")
    

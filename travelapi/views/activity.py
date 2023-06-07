from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Activity, ActivityItinerary, Trip


class ActivityView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """

        activity = Activity.objects.get(pk=pk)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        activities = Activity.objects.all()
        trip_id = request.query_params.get('trip', None)
        name = request.query_params.get('name', None)
        if name is not None:
            activities = Activity.objects.filter(name__icontains = name)
        if trip_id is not None:
           # trip = Trip.objects.get(pk=trip_id)
            activities = Activity.objects.filter(
                activity_itinerary__trip=trip_id)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Activity instance
        """
        serializer = CreateActivitySerializer(data=request.data)
        # serializer = CreateTripActivitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        

class CreateActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', "location", "cost"]
# class CreateTripActivitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ActivityItinerary
#         fields = ['id', 'trip', "location", "activity"]
class ActivitySerializer(serializers.ModelSerializer):
    """JSON serializer for Activities
    """
    class Meta:
        model = Activity
        fields = ('id', 'name', "location", "cost", "activity_itinerary")
        depth = 1
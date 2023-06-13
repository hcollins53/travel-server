from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Trip, Location, TripLocation, Activity, ActivityItinerary
from django.contrib.auth.models import User
from rest_framework.decorators import action

class TripView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """
        try:
            trip = Trip.objects.get(pk=pk)
            # tripLocations = TripLocation.objects.filter(trip=trip.id)
            # trip.locations.set(trip_location.location.id for trip_location in tripLocations)
            serializer = TripSerializer(trip)
            return Response(serializer.data)
        except Trip.DoesNotExist as ex:
            return Response({"reason": ex.message}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        trips = Trip.objects.all()
        user_id = request.query_params.get('user', None)
        
        if user_id is not None:
            user = User.objects.get(pk=user_id)
            trips = Trip.objects.filter(user=user)
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized trip instance
        """
        serializer = CreateTripSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    @action(methods=['post'], detail=True)
    def location(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        location = Location.objects.get(pk=request.data["location"])
        trip_location = TripLocation(trip=trip, location=location)
        trip_location.save()
        trip.locations.add(trip_location)
        return Response({'message': 'Location added'}, status=status.HTTP_201_CREATED)
    @action(methods=['post'], detail=True)
    def activity(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        location = Location.objects.get(pk=request.data["location"])
        activity = Activity.objects.get(pk=request.data["activity"])
        trip_activity = ActivityItinerary(trip=trip, location=location, activity=activity)
        trip_activity.save()
        trip.details.add(trip_activity)
        return Response({'message': 'Activity added'}, status=status.HTTP_201_CREATED)
    @action(methods=['delete'], detail=True)
    def delete_activity(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        activity = ActivityItinerary.objects.get(activity=request.data["activity"], trip=trip.id)
        trip.details.remove(request.data["activity"])
        activity.delete()
        return Response({'message': 'Activity Deleted'}, status=status.HTTP_204_NO_CONTENT)
class CreateTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'name', 'user', 'start_date', "end_date", "image"]
class TripLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripLocation
        fields = ["id", "location_name", "location"]
class TripActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityItinerary
        fields = ["id", "location_name", "location", "activity", "activity_name"]
class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for trips
    """
    locations = TripLocationSerializer(many=True)
    details = TripActivitySerializer(many=True)
    class Meta:
        model = Trip
        fields = ('id', 'name', 'start_date', "end_date", "user", "locations", "details", "image")
    
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Trip


class TagView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """

        trip = Trip.objects.get(pk=pk)
        serializer = TripSerializer(trip)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized trip instance
        """

        new_trip = Trip()
        new_trip.name = request.data['name']
        new_trip.dates = request.data['dates']
        new_trip.save()

        serialized = TripSerializer(new_trip)

        return Response(serialized.data, status=status.HTTP_201_CREATED)
        
        


class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for trips
    """
    class Meta:
        model = Trip
        fields = ('id', 'name', 'dates')
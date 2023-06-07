from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Itinerary, ActivityItinerary


class ItineraryView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """

        itinerary = Itinerary.objects.get(pk=pk)
        serializer = ItinerarySerializer(itinerary)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        itineraries = Itinerary.objects.all()
        serializer = ItinerarySerializer(itineraries, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Itinerary instance
        """
        all_details = []
        details = request.data["details"]
        for detail in details:
            trip_detail = ActivityItinerary.objects.get(pk=detail)
            all_details.append(trip_detail)
        serializer = CreateItinerarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(details=all_details)


        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        

class CreateItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = ['id', 'trip', "details"]
class ItinerarySerializer(serializers.ModelSerializer):
    """JSON serializer for Itinerarys
    """
    class Meta:
        model = Itinerary
        fields = ('id', "trip", "details")
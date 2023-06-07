from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Location, TripLocation


class LocationView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """

        location = Location.objects.get(pk=pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        locations = Location.objects.all()
        name = request.query_params.get('name', None)
        
        if name is not None:
            locations = Location.objects.filter(name=name)
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Location instance
        """

        serializer = CreateLocationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        

class CreateLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']
class LocationSerializer(serializers.ModelSerializer):
    """JSON serializer for Locations
    """
    class Meta:
        model = Location
        fields = ('id', "name")
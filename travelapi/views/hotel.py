from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Hotel


class HotelView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """

        hotel = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        hotels = Hotel.objects.all()
        location_id = request.query_params.get('trip', None)
        name = request.query_params.get('name', None)
        if name is not None:
            hotels = Hotel.objects.filter(name__icontains = name)
        if location_id is not None:
            hotels = Hotel.objects.filter(trip=location_id)
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Hotel instance
        """
        serializer = CreateHotelSerializer(data=request.data)
        # serializer = CreateTripHotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request, pk):
        
        hotel = Hotel.objects.get(pk=pk)
        #self.check_object_permissions(request, review)
        hotel.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    
        

class CreateHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', "location", "place_id", "rating", "vicinity", "lat", "lng"]
# class CreateTripHotelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HotelItinerary
#         fields = ['id', 'trip', "location", "Hotel"]
class HotelSerializer(serializers.ModelSerializer):
    """JSON serializer for Activities
    """
    class Meta:
        model = Hotel
        fields = ('id', 'name', "location", "place_id", "rating", "vicinity", "lat", "lng")
        depth = 1
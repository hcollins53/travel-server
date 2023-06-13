from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Travel


class TransportationView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """

        travel = Travel.objects.get(pk=pk)
        serializer = TravelSerializer(travel)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        travels = Travel.objects.all()
        trip_id = request.query_params.get('trip', None)
        name = request.query_params.get('name', None)
        if name is not None:
            travels = Travel.objects.filter(name__icontains = name)
        if trip_id is not None:
            travels = Travel.objects.filter(trip=trip_id)
        serializer = TravelSerializer(travels, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Travel instance
        """
        serializer = CreateTravelSerializer(data=request.data)
        # serializer = CreateTripTravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request, pk):
        
        travel = Travel.objects.get(pk=pk)
        #self.check_object_permissions(request, review)
        travel.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    
        

class CreateTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ['id', 'trip', "dep_date", "transport_type", "dep_time", "arr_time", "dep_location", "arr_location"]

class TravelSerializer(serializers.ModelSerializer):
    """JSON serializer for Activities
    """
    class Meta:
        model = Travel
        fields = ('id', 'trip', "dep_date", "transport_type", "dep_time", "arr_time", "dep_location", "arr_location")
        depth = 1
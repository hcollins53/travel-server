from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Packing


class PackingView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """

        packing = Packing.objects.get(pk=pk)
        serializer = PackingSerializer(packing)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        packings = Packing.objects.all()
        trip_id = request.query_params.get('trip', None)
        if trip_id is not None:
           # trip = Trip.objects.get(pk=trip_id)
            packings = Packing.objects.filter(trip=trip_id)
        serializer = PackingSerializer(packings, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Packing instance
        """
        serializer = CreatePackingSerializer(data=request.data)
        # serializer = CreateTripPackingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request, pk):
        
        packing = Packing.objects.get(pk=pk)
        #self.check_object_permissions(request, review)
        packing.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    
        

class CreatePackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packing
        fields = ['id', "trip", "item", "amount"]
# class CreateTripPackingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PackingItinerary
#         fields = ['id', 'trip', "location", "Packing"]
class PackingSerializer(serializers.ModelSerializer):
    """JSON serializer for Activities
    """
    class Meta:
        model = Packing
        fields = ('id', "trip", "item", "amount")
        depth = 1
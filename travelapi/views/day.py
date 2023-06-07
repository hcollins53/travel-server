from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Day


class DayView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """

        day = Day.objects.get(pk=pk)
        serializer = DaySerializer(day)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        days = Day.objects.all()
        serializer = DaySerializer(days, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Day instance
        """
        serializer = CreateDaySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        

class CreateDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'day', "date"]
class DaySerializer(serializers.ModelSerializer):
    """JSON serializer for Days
    """
    class Meta:
        model = Day
        fields = ('id', "date", "day")
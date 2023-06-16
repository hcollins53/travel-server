from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Spending


class SpendingView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """

        spending = Spending.objects.get(pk=pk)
        serializer = SpendingSerializer(spending)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        spendings = Spending.objects.all()
        budget_id = request.query_params.get('budget', None)
        if budget_id is not None:
            spendings = Spending.objects.filter(budget=budget_id)
        serializer = SpendingSerializer(spendings, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Spending instance
        """
        serializer = CreateSpendingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        

class CreateSpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spending
        fields = ['id', 'expense', "amount", "budget"]
class SpendingSerializer(serializers.ModelSerializer):
    """JSON serializer for Spendings
    """
    class Meta:
        model = Spending
        fields = ('id', "expense", "amount", "budget")
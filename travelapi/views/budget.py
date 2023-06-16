from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Budget, Trip, Spending


class BudgetView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized user
        """

        budget = Budget.objects.get(pk=pk)
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        budgets = Budget.objects.all()
        trip_id = request.query_params.get('trip', None)
        if trip_id is not None:
            budgets = Budget.objects.filter(trip=trip_id)
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Budget instance
        """
        serializer = CreateBudgetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        

class CreateBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'trip', "amount"]
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ["id", "name"]
class BudgetSerializer(serializers.ModelSerializer):
    """JSON serializer for Budgets
    """
    class Meta:
        model = Budget
        fields = ('id', "trip", "amount", "expenses")
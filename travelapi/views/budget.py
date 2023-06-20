from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from travelapi.models import Budget, Trip, Spending, TripExpenses
from rest_framework.decorators import action
from django.db.models import Count, Q

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
        # .annotate(total_spending=Count('expenses__spending_amount'))
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
    @action(methods=['post'], detail=True)  
    def expense(self, request, pk):
        budget = Budget.objects.get(pk=pk)
        spending = Spending.objects.get(pk=request.data["spending"])
        spending_expense = TripExpenses(budget=budget, spending=spending)
        spending_expense.save()
        budget.expenses.add(spending_expense)
        return Response({'message': 'Expense added'}, status=status.HTTP_201_CREATED)    

class CreateBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'trip', "amount"]
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ["id", "name"]
class TripExpensesSerializer(serializers.ModelSerializer):
    model = TripExpenses
    fields = ["id", "budget", "spending", "spending_amount"]
class BudgetSerializer(serializers.ModelSerializer):
    """JSON serializer for Budgets
    """
    trip = TripSerializer(many=False)
    expenses = TripExpensesSerializer(many=True)
    class Meta:
        model = Budget
        fields = ('id', "trip", "amount", "expenses")
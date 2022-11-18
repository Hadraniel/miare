from rest_framework import serializers
from courier.serializers import CourierSerializer
from income.models import WeeklyIncome


class WeeklyIncomeSerializer(serializers.ModelSerializer):
    couriers = CourierSerializer(read_only=True)

    class Meta:
        model = WeeklyIncome
        fields = "__all__"

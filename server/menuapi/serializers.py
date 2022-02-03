from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    # order_date = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # dish = serializers.CharField(source='dish.title')

    # def create(self, validated_data):
    #     total_sum = validated_data['amount'] * validated_data['amount']
    #     return Order.objects.create(**validated_data, total_sum=total_sum)

    class Meta:
        model = Order
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


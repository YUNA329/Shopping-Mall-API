from rest_framework import serializers
from .models import Order, OrderItem

class ItemRequestSerializer(serializers.Serializer):
    itemId = serializers.IntegerField()
    count = serializers.IntegerField()

class OrderRequestSerializer(serializers.Serializer):
    memberId = serializers.IntegerField()   
    items = ItemRequestSerializer(many=True)

class OrderItemSerializer(serializers.Serializer):
    itemId =serializers.IntegerField(source='item.id')
    itemName = serializers.CharField(source='item.item_name')
    itemPrice = serializers.IntegerField(source='item.item_price')
    count = serializers.IntegerField()
    
    class Meta:
        model = OrderItem
        fields = ['itemId', 'itemName', 'itemPrice', 'count']

class OrderSerializer(serializers.Serializer):
    orderId = serializers.IntegerField(source='id')
    memberId = serializers.IntegerField(source='member.id')
    orderDate = serializers.DateTimeField(source = 'order_date')
    items = OrderItemSerializer(source='order_items',many=True)
    status = serializers.CharField()
    
    class Meta:
        model = Order
        fields = ['orderId', 'memberId', 'orderDate', 'items', 'status']
    
    

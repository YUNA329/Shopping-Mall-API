from django.db import models
from members.models import Member
from items.models import Item


# Create your models here.

class Order(models.Model):
   order_date = models.DateTimeField(auto_now_add=True)
   member = models.ForeignKey(Member, on_delete=models.CASCADE)
   item = models.ManyToManyField(Item, through='OrderItem')
   status = models.CharField(max_length=50, default='ordered')
   
   class Meta:
       db_table = 'orders'
       
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField()
    
    
    class Meta:
        db_table = 'order_items'

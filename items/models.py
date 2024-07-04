from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()
    stock_quantity = models.IntegerField()
    
    class Meta:
        db_table = 'item'
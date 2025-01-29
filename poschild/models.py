from django.db import models
from posmaster.models import PosMaster
# Create your models here.
class PosChild(models.Model):
    
    pos_master = models.ForeignKey(PosMaster, on_delete=models.CASCADE, related_name='products')  # Foreign key to PosMaster
    item_name = models.CharField(max_length=100)  # Item Name
    qty = models.IntegerField()  # Quantity
    mrp = models.DecimalField(max_digits=10, decimal_places=2)  # MRP
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)  # Sale Price
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total for the item
    
class meta:
    db_table="tbl_child"
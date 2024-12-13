from django.db import models

# Create your models here.
class ProductModel(models.Model):
    pname=models.CharField(max_length=255)
    hsncode=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    brand=models.CharField(max_length=255)
    tax=models.CharField(max_length=255)
    punit=models.CharField(max_length=255)
    aunit=models.CharField(max_length=255)
    class Meta:
        db_table = 'tbl_product'
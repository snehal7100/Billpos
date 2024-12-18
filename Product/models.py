from django.db import models

class ProductModel(models.Model):
    pid=models.CharField(max_length=255)
    pname=models.CharField(max_length=255)
    hsncode=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    brand=models.CharField(max_length=255)
    tax=models.CharField(max_length=255)
    taxtype=models.CharField(max_length=255)
    punit=models.CharField(max_length=255)
    aunit=models.CharField(max_length=255)
    cfactor = models.CharField(max_length=255, default='1')
    price=models.CharField(max_length=255, default='1')

    class Meta:

        db_table = 'tbl_product'


from django.db import models

class ProductModel(models.Model):
    pid= models.CharField(max_length=255)
    pname = models.CharField(max_length=255)
    hsncode = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    taxtype = models.CharField(max_length=255, default="standard")  # Set default value here
    punit = models.CharField(max_length=255)
    aunit = models.CharField(max_length=255)
    cfactor = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'tbl_product'

   
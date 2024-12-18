from django.db import models

class ProductModel(models.Model):
<<<<<<< HEAD

    pname = models.CharField(max_length=255)
    hsncode = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    taxtype = models.CharField(max_length=255, default="standard")  # Set default value here
    punit = models.CharField(max_length=255)
    aunit = models.CharField(max_length=255)
    cfactor = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    uprice = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'tbl_product'

    def __str__(self):
        return self.pname

=======
>>>>>>> 402f905256171b4ed8e09e5de2a30224d8b18b23
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


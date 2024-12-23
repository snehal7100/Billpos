from django.db import models

class Suppliers(models.Model):
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    gst_no = models.CharField(max_length=15, null=True, blank=True)
    pan_no = models.CharField(max_length=10, null=True, blank=True)
    opening_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    group_type = models.CharField(max_length=255, null=True, blank=True)
    billing_address = models.TextField()
    shipping_address = models.TextField()
    city = models.CharField(max_length=100)
    credit_limit = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    credit_period = models.PositiveIntegerField(default=0)
    supplier_barcode = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'tbl_supplier'

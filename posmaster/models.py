from django.db import models

class PosMaster(models.Model):
    customer_name = models.CharField(max_length=100)  # Customer Name
    mobile_no = models.CharField(max_length=15)  # Mobile Number
    address = models.TextField()  # Address
    credit_amt = models.DecimalField(max_digits=10, decimal_places=2)  # Credit Amount
    payment_term = models.CharField(max_length=50)  # Payment Term
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total Amount
    bill_date = models.DateField()  # Bill Date

    class Meta:
        db_table = 'tbl_pos_master'

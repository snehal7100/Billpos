from django.db import models
class Payment(models.Model):
    pid=models.CharField(max_length=255,default='1')
    pname=models.CharField(max_length=255)
    class Meta:
        db_table = 'tbl_payment'
# Create your models here.

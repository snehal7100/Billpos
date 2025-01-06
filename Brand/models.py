from django.db import models

class BrandForm(models.Model):
    bid=models.CharField(max_length=255,default='1')
    bname=models.CharField(max_length=255)
    img=models.FileField(upload_to='pics/',max_length=255,null=True)
    class Meta:
        db_table = 'tbl_Brand'
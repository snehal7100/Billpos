from django.db import models

# Create your models here.
class BrandForm(models.Model):
    bname=models.CharField(max_length=255)
    img=models.FileField(upload_to='pics/',max_length=255,null=True)
    class Meta:
        db_table = 'tbl_Brand'
from django.db import models


# Create your models here.
class Category(models.Model):
    
    c_name=models.CharField(max_length=255)
    c_img=models.FileField(upload_to="category/",max_length=255,null=True)
    B_img=models.FileField(upload_to="category/",max_length=255,null=True)
    
    class Meta:
        db_table = 'tbl_category'

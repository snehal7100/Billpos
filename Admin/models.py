from django.db import models

# Create your models here.
class Adminn(models.Model):
    username=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    img=models.FileField(upload_to='pics/',max_length=255,null=True)
    class Meta:
        db_table = 'tbl_AdminForm'
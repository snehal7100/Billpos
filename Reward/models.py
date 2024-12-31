from django.db import models

# Create your models here.
class RewarsPoints(models.Model):
    minrange = models.IntegerField() 
    maxrange = models.IntegerField()  
    points = models.IntegerField()  
    
    
    class Meta:
        db_table = 'tbl_rewards'

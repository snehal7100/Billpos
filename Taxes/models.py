from django.db import models

# Create your models here.
class Taxs(models.Model):
    tid = models.CharField(max_length=255)  # Explicit primary key field
    sr_no = models.CharField(max_length=255)
    taxname = models.CharField(max_length=255)
    taxpercentage = models.CharField(max_length=255)

    class Meta:
<<<<<<< HEAD
        db_table = 'tbl_taxes' 
=======
        db_table = 'tbl_taxes'
>>>>>>> 4ffc9292d0922e5c37b948ac50fc432c183261fd

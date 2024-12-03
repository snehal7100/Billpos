from django.db import models

# Create your models here.
class LoginForm(models.Model):
    uname=models.CharField(max_length=255)
    passw=models.CharField(max_length=255)
    class Meta:
        db_table = 'tbl_Login'
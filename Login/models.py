from django.db import models


# Create your models here.
class LoginForm(models.Model):
    uname=models.CharField(max_length=255)
    passw=models.CharField(max_length=255)
    # img=models.ImageField(upload_to='pics',default='default.svg')
    class Meta:
        db_table = 'tbl_Login'
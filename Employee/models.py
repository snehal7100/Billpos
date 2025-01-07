from django.db import models

# Create your models here.
class Employee(models.Model):
    membername=models.CharField(max_length=255)
    mobno=models.CharField(max_length=255)
    emobno=models.CharField(max_length=255)
    emaileadd=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    salary=models.CharField(max_length=255)
    datejoining=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    lastexperience=models.CharField(max_length=255)
    lastworkcom=models.CharField(max_length=255)
    lastcomsalary=models.CharField(max_length=255)
    adharnum=models.CharField(max_length=255)
    pannum=models.CharField(max_length=255)
    userupi=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    adharimg=models.FileField(upload_to="Employee/",max_length=255,null=True)
    panimg=models.FileField(upload_to="Employee/",max_length=255,null=True)
    proimg=models.FileField(upload_to="Employee/",max_length=255,null=True)
    qrimg=models.FileField(upload_to="Employee/",max_length=255,null=True)
    
    class Meta:
        db_table = 'tbl_Employee'

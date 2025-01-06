from django.contrib import admin
from Employee.models import Employee
# Register your models here.
class EmployeAdmin(admin.ModelAdmin):
    list_display=("id","membername","mobno","emobno","emaileadd","password","salary","datejoining","department","role",
                  "lastexperience","lastworkcom","lastcomsalary","adharnum","pannum","userupi","address","adharimg","panimg","proimg","qrimg")
admin.site.register(Employee,EmployeAdmin)

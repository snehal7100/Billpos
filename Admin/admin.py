from django.contrib import admin
from Admin.models import Adminn

class AdminLog(admin.ModelAdmin):
    list_display=("username","email","img",)
admin.site.register(Adminn,AdminLog)
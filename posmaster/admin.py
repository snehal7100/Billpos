from django.contrib import admin

# Register your models here.
from posmaster.models import PosMaster
class posm(admin.ModelAdmin):
    list_display=("customer_name","mobile_no","address","credit_amt","payment_term","total","bill_date")
admin.site.register(PosMaster,posm)
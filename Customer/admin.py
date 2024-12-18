from django.contrib import admin
from .models import Customer  

class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "mobile_no", 
        "email", 
        "gst_no", 
        "pan_no", 
        "opening_balance", 
        "group_type", 
        "billing_address", 
        "shipping_address", 
        "city", 
        "credit_limit", 
        "credit_period", 
        "customer_barcode",
    )
    

admin.site.register(Customer, CustomerAdmin)

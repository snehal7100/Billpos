from django.contrib import admin
from Supplier.models import Suppliers

class SupplierAdmin(admin.ModelAdmin):
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
        "supplier_barcode",
    )

admin.site.register(Suppliers, SupplierAdmin)

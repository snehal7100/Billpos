from django.contrib import admin
from Taxes.models import Taxs

class TaxsAdmin(admin.ModelAdmin):
    list_display = ('id','sr_no', 'taxname', 'taxpercentage')  


admin.site.register(Taxs,TaxsAdmin)

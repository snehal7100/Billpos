from django.contrib import admin

# Register your models here.
from poschild.models import PosChild
class PosChildAdmin(admin.ModelAdmin):
    list_display = ("pos_master","item_name", "qty", "mrp", "sale_price", "total")

admin.site.register(PosChild,PosChildAdmin)
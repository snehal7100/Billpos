from django.contrib import admin

# Register your models here.
from Brand.models import BrandForm
class BrandAdmin(admin.ModelAdmin):
    list_display=("bid","bname","img",)
admin.site.register(BrandForm,BrandAdmin)
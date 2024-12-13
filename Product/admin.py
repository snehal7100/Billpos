from django.contrib import admin
from Product.models import ProductModel

class productAdmin(admin.ModelAdmin):
    list_display=("pname","hsncode","category","brand","tax","punit","aunit",)
admin.site.register(ProductModel,productAdmin)
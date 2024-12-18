from django.contrib import admin
from Product.models import ProductModel

class productAdmin(admin.ModelAdmin):
    list_display=("pid","pname","hsncode","category","brand","tax","taxtype","punit","aunit","cfactor","price",)
admin.site.register(ProductModel,productAdmin)
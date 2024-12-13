from django.contrib import admin
from Product.models import ProductModel

class productAdmin(admin.ModelAdmin):
    list_display=("pname","hsncode","category","brand","tax","taxtype","punit","aunit","cfactor","uprice",)
admin.site.register(ProductModel,productAdmin)
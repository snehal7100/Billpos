from django.contrib import admin


from Admin.models import product

class productAdmin(admin.ModelAdmin):
    list_display=("pname","hsncode","category","brand","tax","punit","aunit",)
admin.site.register(product,productAdmin)
from django.contrib import admin
from category.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=("cid","c_name","c_img","B_img")
admin.site.register(Category,CategoryAdmin)

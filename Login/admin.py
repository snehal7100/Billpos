from django.contrib import admin

# Register your models here.
from Login.models import LoginForm

class LoginAdmin(admin.ModelAdmin):
    list_display=("uname","passw",)
admin.site.register(LoginForm,LoginAdmin)
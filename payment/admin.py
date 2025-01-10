from django.contrib import admin

# Register your models here.
from payment.models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display=("pid","pname")
admin.site.register(Payment,PaymentAdmin)
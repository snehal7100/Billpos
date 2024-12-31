from django.contrib import admin
from Reward.models import RewarsPoints
# Register your models here.

class RewardsandPoints(admin.ModelAdmin):
    list_display=("minrange","maxrange","points",)
admin.site.register(RewarsPoints,RewardsandPoints)
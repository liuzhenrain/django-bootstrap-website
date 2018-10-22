from django.contrib import admin
from .models import AppleAccountModel
# Register your models here.


class AppleAccountAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('帐号', {"fields":['apple_account']}),
    #     ('是否可用', {"fields":['can_use']}),
    # ]
    list_display = ('apple_account','small_game','used','create_date')
    list_filter = ['used']


admin.site.register(AppleAccountModel, AppleAccountAdmin)

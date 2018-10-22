from django.contrib import admin
from .models import AppleAccountModel,AccountEventModel
# Register your models here.

class AccountEventModelInline(admin.TabularInline):
    '''Tabular Inline View for AccountEventModel'''

    model = AccountEventModel
    extra = 0

class AppleAccountAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('帐号', {"fields":['apple_account']}),
    #     ('是否可用', {"fields":['can_use']}),
    # ]
    inlines = [AccountEventModelInline]
    list_display = ('apple_account','small_game','used','status','create_date')
    list_filter = ['used']


admin.site.register(AppleAccountModel, AppleAccountAdmin)

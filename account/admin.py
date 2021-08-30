from .models import Account
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('phoneNumber','username','email','date_joined','last_login')
    search_fields = ('phoneNUmber','username','email')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal =  ()
    list_filter= ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)





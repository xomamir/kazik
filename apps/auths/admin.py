from django.contrib import admin

from .models import (
    MyUserManager,
    MyUser,
    ActivationCode,
    BankCard,
    Transaction,

)

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'nickname', 'currency', 'balance']
    list_filter = ['email', 'nickname', 'currency']
    ordering = ['email', 'nickname']


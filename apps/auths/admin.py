from django.contrib import admin


from auths.models.bank_card import (BankCard)
from auths.models.my_user import (MyUserManager,MyUser,Transaction)


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'nickname', 'currency', 'balance']
    list_filter = ['email', 'nickname', 'currency']
    ordering = ['email', 'nickname']


admin.site.register(Transaction)

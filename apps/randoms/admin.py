from django.contrib import admin

from .models import Banner, Bet


# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'name',
        'is_active',
        'banner_file'
    )
    list_filter: list[str] = (
        'name',
    )   

admin.site.register(Banner, BannerAdmin)
admin.site.register(Bet)
from django.contrib import admin
from .models import Ads


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'channel',
        'budget',
    )
    list_display_links = (
        'name',
    )
    list_editable = (
        'product',
        'budget'
    )
    ordering = ('id',)

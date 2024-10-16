from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'surname',
        'last_name',
        'email',
        'phone',
        'ad',
        'contract',
    )
    list_display_links = (
        'first_name',
        'surname',
        'last_name',
    )
    list_editable = ('ad', 'contract')
    ordering = ('id',)

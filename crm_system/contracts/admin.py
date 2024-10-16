from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'document',
        'description',
        'cost',
        'created_by',
        'start_date',
        'end_date',
    )
    list_display_links = (
        'name',
    )
    list_editable = (
        'product',
        'start_date',
        'end_date'
    )
    ordering = ('id',)

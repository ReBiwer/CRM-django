from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'surname',
        'last_name',
        'email',
        'phone',
        'ad',
    )
    list_display_links = (
        'first_name',
        'surname',
        'last_name',
    )
    list_editable = ('ad',)
    ordering = ('id',)

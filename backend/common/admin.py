from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Client, Lead, Newsletter


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'client_info',
        'team_id',
        'monthly_charge',
        'one_time_charge',
        'category',
    )
    search_fields = (
        'client_info',
        'team_id',
    )
    list_filter = ('category',)
    ordering = ('client_info',)



@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'company_name',
        'position',
        'email',
        'phone_number',
        'source',
        'status',
        'category',
        'created_at',
    )
    search_fields = (
        'full_name',
        'company_name',
        'email',
        'phone_number',
    )
    list_filter = ('source', 'status', 'category')
    ordering = ('-created_at',)

@admin.register(Newsletter)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_subscribed')
    search_fields = ('email',)
    list_filter = ('is_subscribed',)
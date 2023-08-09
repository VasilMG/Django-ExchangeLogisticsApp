from django.contrib import admin

from ExchangeLogistics.exchange.models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['created_on','loading_date', 'loading_country','unloading_date', 'unloading_country', 'company']
    list_filter = ('company',)
    list_per_page = 10

# @admin.register(Support)
# class SupportAdmin(admin.ModelAdmin):
#     list_display = ['support_email', 'phone_number']

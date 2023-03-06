from django.contrib import admin

from ExchangeLogistics.exchange.models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['created_on', 'company']

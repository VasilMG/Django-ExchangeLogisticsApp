from django.contrib import admin

from ExchangeLogistics.common.models import ServicesData, NetworkData, AboutData


@admin.register(ServicesData)
class ServicesDataAdmin(admin.ModelAdmin):
    list_display = ['service_type']

@admin.register(NetworkData)
class NetworkDataAdmin(admin.ModelAdmin):
    list_display = ['country']


@admin.register(AboutData)
class AboutDataAdmin(admin.ModelAdmin):
    pass

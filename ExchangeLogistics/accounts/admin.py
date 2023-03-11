from django.contrib import admin

from ExchangeLogistics.accounts.models import CustomUser, CompanyProfile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['user' , 'company_name', 'country', 'company_email']
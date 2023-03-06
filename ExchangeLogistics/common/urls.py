from django.urls import path

from ExchangeLogistics.common.views import index, services, network, about

urlpatterns = [
    path('', index, name='index'),
    path('services/', services, name='services_main'),
    path('newtwork/', network, name='network'),
    path('about/', about, name='about'),

]

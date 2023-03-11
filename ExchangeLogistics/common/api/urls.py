from django.urls import path

from ExchangeLogistics.common.api.views import IndexApiView, ServicesApiView, AboutDataApiView

urlpatterns = [
    path('index/', IndexApiView.as_view(), name='api_index'),
    path('services/', ServicesApiView.as_view(), name='api_services'),
    path('about/', AboutDataApiView.as_view(), name='api_about'),
]


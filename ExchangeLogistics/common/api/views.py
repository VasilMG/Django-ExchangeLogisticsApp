from rest_framework import generics as rest_views

from ExchangeLogistics.common.api.serializers import IndexDataSerializer, ServicesDataSerializer, AboutDataSerializer
from ExchangeLogistics.common.models import ServicesData, AboutData


class IndexApiView(rest_views.ListAPIView):
    queryset = ServicesData.objects.all()
    serializer_class = IndexDataSerializer

class ServicesApiView(rest_views.ListAPIView):
    queryset = ServicesData.objects.all()
    serializer_class = ServicesDataSerializer

class AboutDataApiView(rest_views.ListAPIView):
    queryset = AboutData.objects.all()
    serializer_class = AboutDataSerializer
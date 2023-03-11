from rest_framework import serializers

from ExchangeLogistics.common.models import ServicesData, AboutData


class IndexDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesData
        fields = ['service_type', 'short_text']


class ServicesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesData
        exclude = ['short_text']


class AboutDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutData
        fields = '__all__'

from rest_framework import serializers
from .models import *


class ProductBarCodeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ProductBarCode.
    """
    company_name = serializers.CharField(source='company.id')
    company_certificate_type = serializers.CharField(source='company.certificate_type')

    class Meta:
        model = ProductBarCode
        fields = ['id', 'code', 'bar_type', 'product_status', 'company_name', 'company_certificate_type', 'adal_center_icon', 'product_image', 'product_name']

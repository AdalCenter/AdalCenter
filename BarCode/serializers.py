from rest_framework import serializers
from .models import *


class ProductBarCodeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name')
    company_id = serializers.CharField(source='company.id')

    class Meta:
        model = ProductBarCode
        fields = ['id', 'code', 'bar_type', 'product_status', 'company_name', 'company_id']

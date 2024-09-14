from rest_framework import serializers
from .models import *

class ObserverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observer
        fields = '__all__'

class CertifiedCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CertifiedCompany
        exclude = ['certificate_type']

class CertifiedCompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertifiedCompany
        fields = ['company_photo', 'trademark', 'registration_number', 'company_name', 'certificate_type']

class ServiceSerializer(serializers.ModelSerializer):
    companies = CertifiedCompanyListSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'photo', 'service', 'companies']


from rest_framework import serializers
from .models import CertifiedCompany, Service, Observer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service', 'photo']

class ObserverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observer
        fields = ['id', 'name', 'contact_number', 'address', 'certificate_duration']

class CertifiedCompanyListSerializer(serializers.ModelSerializer):
    service_type = ServiceSerializer(read_only=True)
    observer = ObserverSerializer(read_only=True)

    class Meta:
        model = CertifiedCompany
        fields = [
        'id', 'company_email', 'certificate_name', 'company_photo', 'company_name', 'trademark', 'service_type', 'registration_number', 
        'region', 'observer', 'company_address', 'certificate_photo', 'qr_code', 'issue_date', 'expiration_date', 'certificate_type'
        ]

from rest_framework import serializers
from .models import CertifiedCompany, Service, Observer
from django.utils import timezone


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service', 'photo']

class ObserverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observer
        fields = ['id', 'fullname', 'observer_profile_image', 'contact_number', 'address']

class CertifiedCompanyListSerializer(serializers.ModelSerializer):
    service_type = ServiceSerializer(read_only=True)
    observer = ObserverSerializer(read_only=True)
    time_until_expiration = serializers.SerializerMethodField()

    class Meta:
        model = CertifiedCompany
        fields = [
            'id', 'company_email', 'certificate_name', 'company_photo', 'company_name', 'trademark', 'service_type', 
            'registration_number', 'region', 'observer', 'company_address', 'certificate_photo', 'qr_code', 
            'issue_date', 'expiration_date', 'certificate_type', 'time_until_expiration', 'certificate_status_date_icon', 'certificate_status_date_text'
        ]

    def get_time_until_expiration(self, obj):
        now = timezone.now()
        expiration_datetime = obj.expiration_date
        time_delta = expiration_datetime - now
        
        if time_delta.total_seconds() > 0:
            days = time_delta.days
            hours, remainder = divmod(time_delta.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
        else:
            days, hours, minutes = 0, 0, 0
        
        if days <= 10:
            color = 'red'
        elif days <= 30:
            color = 'orange'
        else:
            color = 'green'

        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'color': color
        }

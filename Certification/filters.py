import django_filters
from .models import *


class CertifiedCompanyFilter(django_filters.FilterSet):
    company_name = django_filters.CharFilter(field_name='company_name', lookup_expr='icontains', label='Название компании')
    region = django_filters.ChoiceFilter(field_name='region', choices=[(region, region) for region in CertifiedCompany.objects.values_list('region', flat=True).distinct()], label='Регион')
    service_type = django_filters.ChoiceFilter(field_name='service_type__service', choices=[(service, service) for service in Service.objects.values_list('service', flat=True).distinct()], label='Тип услуги')
    observer = django_filters.ChoiceFilter(field_name='observer__fullname', choices=[(fullname, fullname) for fullname in Observer.objects.values_list('fullname', flat=True).distinct()], label='Наблюдатель')
    certificate_type = django_filters.ChoiceFilter(field_name='certificate_type', choices=[(cert_type, cert_type) for cert_type in CertifiedCompany.objects.values_list('certificate_type', flat=True).distinct()], label='Статус сертификата')

    class Meta:
        model = CertifiedCompany
        fields = ['company_name', 'region', 'service_type', 'observer', 'certificate_type']


import django_filters
from .models import *


class CertifiedCompanyFilter(django_filters.FilterSet):
    company_name = django_filters.CharFilter(field_name='company_name', lookup_expr='icontains', label='Название компании')
    region = django_filters.ChoiceFilter(field_name='region', choices=CertifiedCompany.objects.all().values_list('region', 'region').distinct(), label='Регион')
    service_type = django_filters.ChoiceFilter(field_name='service_type', choices=Service.objects.all().values_list('service', 'service').distinct(), label='Тип услуги')
    observer = django_filters.ChoiceFilter(field_name='observer', choices=Observer.objects.all().values_list('name', 'name').distinct(), label='Наблюдатель')
    certificate_type = django_filters.ChoiceFilter(field_name='certificate_type', choices=CertifiedCompany.objects.all().values_list('certificate_type', 'certificate_type').distinct(), label='Статус сертификата')

    class Meta:
        model = CertifiedCompany
        fields = ['company_name', 'region', 'service_type', 'observer', 'certificate_type']

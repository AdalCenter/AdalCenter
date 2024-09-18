import django_filters
from .models import *

class CertifiedCompanyFilter(django_filters.FilterSet):
    company_name = django_filters.CharFilter(field_name='company_name', lookup_expr='icontains')
    region = django_filters.CharFilter(field_name='region', lookup_expr='icontains')
    service_type = django_filters.ModelChoiceFilter(queryset=Service.objects.all())
    observer = django_filters.ModelChoiceFilter(queryset=Observer.objects.all())
    certificate_type = django_filters.ChoiceFilter(choices=CertifiedCompany.CERTIFICATE_TYPE_CHOICES)

    class Meta:
        model = CertifiedCompany
        fields = ['company_name', 'region', 'service_type', 'observer', 'certificate_type']

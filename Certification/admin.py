from django.contrib import admin
from .models import Observer, Service, CertifiedCompany


@admin.register(Observer)
class ObserverAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'address', 'certificate_duration')
    search_fields = ('name', 'contact_number')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service',)
    search_fields = ('service',)

@admin.register(CertifiedCompany)
class CertifiedCompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'trademark', 'registration_number', 'region', 'certificate_type')
    search_fields = ('company_name', 'trademark', 'registration_number')
    list_filter = ('certificate_type', 'service_type')

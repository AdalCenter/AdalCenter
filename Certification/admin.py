from django.contrib import admin
from .models import Observer, Service, CertifiedCompany
from modeltranslation.admin import TranslationAdmin


@admin.register(Observer)
class ObserverAdmin(TranslationAdmin):
    list_display = ('fullname', 'contact_number', 'address')
    search_fields = ('fullname', 'contact_number')

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('service',)
    search_fields = ('service',)

@admin.register(CertifiedCompany)
class CertifiedCompanyAdmin(TranslationAdmin):
    list_display = ('company_name', 'registration_number', 'certificate_name', 'company_email', 'certificate_type', 'region')
    search_fields = ('company_name', 'registration_number', 'certificate_name', 'company_email')
    list_filter = ('certificate_type', 'region')

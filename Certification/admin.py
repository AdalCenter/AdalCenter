from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import CertifiedCompany, Service, Observer
from .translation import *


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('service',)

@admin.register(Observer)
class ObserverAdmin(TranslationAdmin):
    list_display = ('fullname', 'contact_number', 'address')
    search_fields = ('fullname', 'contact_number', 'address')

@admin.register(CertifiedCompany)
class CertifiedCompanyAdmin(TranslationAdmin):
    list_display = ('company_name', 'certificate_name', 'trademark', 'certificate_type', 'region', 'expiration_date')
    search_fields = ('company_name', 'certificate_name', 'trademark', 'region')
    list_filter = ('certificate_type', 'region', 'expiration_date')

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:
            return readonly_fields + ('get_certificate_status_icon', 'get_certificate_status_text')
        return readonly_fields

    def get_certificate_status_icon(self, obj):
        return f'<img src="{obj.get_certificate_status_icon()}" alt="Certificate Status" />'
    
    get_certificate_status_icon.allow_tags = True
    get_certificate_status_icon.short_description = 'Иконка статуса сертификата'

    def get_certificate_status_text(self, obj):
        return obj.get_certificate_status_text()
    
    get_certificate_status_text.short_description = 'Текст статуса сертификата'

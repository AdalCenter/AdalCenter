from modeltranslation.translator import register, TranslationOptions
from .models import Observer, Service, CertifiedCompany


@register(Observer)
class ObserverTranslationOptions(TranslationOptions):
    fields = ('fullname', 'contact_number', 'address',)

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('service',)

@register(CertifiedCompany)
class CertifiedCompanyTranslationOptions(TranslationOptions):
    fields = (
        'company_email', 'certificate_name', 'company_name', 'trademark',
        'company_address', 'certificate_type'
    )

from modeltranslation.translator import register, TranslationOptions
from .models import CertifiedCompany

@register(CertifiedCompany)
class CertifiedCompanyTranslationOptions(TranslationOptions):
    fields = ('certificate_name', 'company_name', 'trademark', 'region', 'company_address', 'certificate_type')

from modeltranslation.translator import translator, TranslationOptions
from .models import ECode


class ECodeTranslationOptions(TranslationOptions):
    fields = ('code_name', 'description')

translator.register(ECode, ECodeTranslationOptions)

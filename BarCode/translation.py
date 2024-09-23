from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(ProductBarCode)
class ProductBarCodeTranslationOptions(TranslationOptions):
    fields = ('code', 'product_name', 'company',)
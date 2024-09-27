from modeltranslation.translator import register, TranslationOptions
from .models import ProductBarCode


@register(ProductBarCode)
class ProductBarCodeTranslationOptions(TranslationOptions):
    fields = ('product_name', 'bar_type', 'product_status')

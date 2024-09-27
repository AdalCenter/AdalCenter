from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import ProductBarCode


@admin.register(ProductBarCode)
class ProductBarCodeAdmin(TranslationAdmin):
    list_display = (
        'product_name', 'bar_type', 'product_status', 'company', 'code'
    )
    search_fields = ('product_name', 'code', 'company__company_name')
    list_filter = ('bar_type', 'product_status', 'company')

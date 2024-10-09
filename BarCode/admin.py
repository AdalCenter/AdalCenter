from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import ProductBarCode
from .translation import *


@admin.register(ProductBarCode)
class ProductBarCodeAdmin(TranslationAdmin):
    list_display = ('product_name', 'code', 'bar_type', 'product_status', 'company')
    search_fields = ('product_name', 'code', 'company__company_name')
    list_filter = ('bar_type', 'product_status', 'company')

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import ProductBarCode
from .translation import *


@admin.register(ProductBarCode)
class ProductBarCodeAdmin(TranslationAdmin):
    list_display = ('product_name', 'code', 'bar_type', 'product_status', 'company')
    search_fields = ('product_name', 'code', 'company__company_name')
    list_filter = ('bar_type', 'product_status', 'company')

    # fieldsets = (
    #     (None, {
    #         'fields': ('code', 'product_name', 'bar_type', 'product_status', 'company')
    #     }),
    #     ('Изображения', {
    #         'fields': ('adal_center_icon', 'product_image'),
    #     }),
    # )

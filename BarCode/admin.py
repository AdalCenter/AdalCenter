from django.contrib import admin
from .models import ProductBarCode


@admin.register(ProductBarCode)
class ProductBarCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'bar_type', 'product_status', 'company')
    search_fields = ('code', 'bar_type', 'product_status')

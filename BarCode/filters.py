from django_filters import rest_framework as filters
from .models import ProductBarCode

class ProductBarCodeFilter(filters.FilterSet):
    """
    Фильтр для модели ProductBarCode.
    """
    code = filters.CharFilter(lookup_expr='icontains')
    bar_type = filters.ChoiceFilter(choices=ProductBarCode._meta.get_field('bar_type').choices)

    class Meta:
        model = ProductBarCode
        fields = ['code', 'bar_type']

from django_filters import rest_framework as filters
from rest_framework import viewsets
from .serializers import *
from .filters import *
from .models import *


class ProductBarCodeViewSet(viewsets.ModelViewSet):
    queryset = ProductBarCode.objects.all()
    serializer_class = ProductBarCodeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductBarCodeFilter
    lookup_field = 'id'

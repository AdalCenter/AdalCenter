from django.urls import path
from .views import ProductBarCodeViewSet


urlpatterns = [
    path('product-barcode/', ProductBarCodeViewSet.as_view({'get': 'list'}), name='product-barcode-list'),
    path('product-barcode/<int:pk>/', ProductBarCodeViewSet.as_view({'get': 'retrieve'}), name='product-barcode-detail'),
]

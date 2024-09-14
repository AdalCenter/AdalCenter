from django.urls import path
from .views import *


urlpatterns = [
    path('code/', ProductBarCodeViewSet.as_view({'get': 'list'})),
    path('code/<int:id>/', ProductBarCodeViewSet.as_view({'get': 'retrieve'})),
]

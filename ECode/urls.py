from django.urls import path
from .views import ECodeViewSet

urlpatterns = [
    path('ecodes/', ECodeViewSet.as_view({'get': 'list', 'post':'create'})),
    path('ecodes/<int:pk>/', ECodeViewSet.as_view({'get': 'retrieve'})),
]

from django.urls import path
from .views import ObserverViewSet, ServiceViewSet, CertifiedCompanyListViewSet, download_certificate, get_filter_options


urlpatterns = [
    path('observers/', ObserverViewSet.as_view({'get': 'list'}), name='observer-list'),
    path('observers/<int:pk>/', ObserverViewSet.as_view({'get': 'retrieve'}), name='observer-detail'),
    path('services/', ServiceViewSet.as_view({'get': 'list'}), name='service-list'),
    path('services/<int:pk>/', ServiceViewSet.as_view({'get': 'retrieve'}), name='service-detail'),
    path('certified-companies/', CertifiedCompanyListViewSet.as_view({'get': 'list'}), name='certified-company-list'),
    path('certified-companies/<int:pk>/', CertifiedCompanyListViewSet.as_view({'get': 'retrieve'}), name='certified-company-detail'),
    path('media/download-certificate/<str:filename>/', download_certificate, name='download_certificate'),
    path('get-filter-options/', get_filter_options, name='get-filter-options'),
]

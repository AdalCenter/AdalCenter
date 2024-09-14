from django.urls import path
from .views import *


urlpatterns = [
    path('observer/', ObserverViewSet.as_view({'get': 'list'}), name='observer'),
    path('service/', ServiceViewSet.as_view({'get': 'list'}), name='service'),
    path('service/<int:pk>/', ServiceCompaniesView.as_view(), name='service-companies'),
    path('certifiedcompany/', CertifiedCompanyListViewSet.as_view({'get': 'list'}), name='certificate-list'),
    path('certifiedcompany/<int:pk>/', CertifiedCompanyDetailView.as_view(), name='certified-company-detail'),
]
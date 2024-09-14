from django.urls import path
from .views import *

urlpatterns = [
    # Coordinates
    path('coordinates/', CoordinateViewSet.as_view({'get': 'list'})),
    path('coordinates/<int:pk>/', CoordinateViewSet.as_view({'get': 'retrieve'})),
    # Contacts
    path('contacts/', ContactViewSet.as_view({'get': 'list'})),
    path('contacts/<int:pk>/', ContactViewSet.as_view({'get': 'retrieve'})),
    # Locate
    path('locate/', LocateViewSet.as_view({'get': 'list'})),
    path('locate/<int:pk>/', LocateViewSet.as_view({'get': 'retrieve'})),
    # Partners
    path('partners/', PartnersViewSet.as_view({'get': 'list'})),
    path('partners/<int:pk>/', PartnersViewSet.as_view({'get': 'retrieve'})),
    # About Us
    path('about-us/', AboutUsViewSet.as_view({'get': 'list'})),
    path('about-us/<int:pk>/', AboutUsViewSet.as_view({'get': 'retrieve'})),
    # FAQ
    path('FAQ/', FAQViewSet.as_view({'get': 'list'})),
    path('FAQ/<int:pk>/', FAQViewSet.as_view({'get': 'retrieve'})),
    # Tez-Kabar Youtube Videos
    path('youtube-videos/', tez_kaber_parsing_videos),
    # Black List Companies
    path('Black-List-Companies/', BlackListCompaniesViewSet.as_view({'get': 'list'})),
    path('Black-List-Companies/<int:pk>/', BlackListCompaniesViewSet.as_view({'get': 'retrieve'})),
]

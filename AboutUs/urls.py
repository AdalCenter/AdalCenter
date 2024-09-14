from django.urls import path
from .views import *


urlpatterns = [
    path('parse-youtube-videos/', tez_kaber_parsing_videos, name='parse-youtube-videos'),
    path('contacts/', ContactViewSet.as_view({'get': 'list'}), name='contact-list'),
    path('contacts/<int:pk>/', ContactViewSet.as_view({'get': 'retrieve'}), name='contact-detail'),
    path('addresses/', AddressViewSet.as_view({'get': 'list'}), name='address-list'),
    path('addresses/<int:pk>/', AddressViewSet.as_view({'get': 'retrieve'}), name='address-detail'),
    path('partners/', PartnerViewSet.as_view({'get': 'list'}), name='partner-list'),
    path('partners/<int:pk>/', PartnerViewSet.as_view({'get': 'retrieve'}), name='partner-detail'),
    path('about-us/', AboutUsViewSet.as_view({'get': 'list'}), name='about-us-list'),
    path('about-us/<int:pk>/', AboutUsViewSet.as_view({'get': 'retrieve'}), name='about-us-detail'),
    path('faqs/', FAQViewSet.as_view({'get': 'list'}), name='faq-list'),
    path('faqs/<int:pk>/', FAQViewSet.as_view({'get': 'retrieve'}), name='faq-detail'),
    path('blacklist-companies/', BlackListCompanyViewSet.as_view({'get': 'list'}), name='blacklist-company-list'),
    path('blacklist-companies/<int:pk>/', BlackListCompanyViewSet.as_view({'get': 'retrieve'}), name='blacklist-company-detail'),
    path('our-achievements/', OurAchievementViewSet.as_view({'get': 'list'}), name='our-achievements-list'),
    path('our-achievements/<int:pk>/', OurAchievementViewSet.as_view({'get': 'retrieve'}), name='our-achievements-detail'),
    path('goals-objectives/', OurGoalsAndObjectivesViewSet.as_view({'get': 'list'}), name='goals-objectives-list'),
    path('goals-objectives/<int:pk>/', OurGoalsAndObjectivesViewSet.as_view({'get': 'retrieve'}), name='goals-objectives-detail'),
    path('team/', OurTeamViewSet.as_view({'get': 'list'}), name='team-list'),
    path('team/<int:pk>/', OurTeamViewSet.as_view({'get': 'retrieve'}), name='team-detail'),
    path('achievement-certificates/', OurAchievementCertificateImageViewSet.as_view({'get': 'list'}), name='achievement-certificates-list'),
    path('achievement-certificates/<int:pk>/', OurAchievementCertificateImageViewSet.as_view({'get': 'retrieve'}), name='achievement-certificates-detail'),
    path('reviews/', ReviewViewSet.as_view({'get': 'list'}), name='reviews-list'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve'}), name='reviews-detail'),
]
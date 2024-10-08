from django.urls import path
from .views import *


urlpatterns = [
    path('parse-youtube-videos/', tez_kabar_parsing_videos, name='parse-youtube-videos'),
    path('footer-contacts/', ContactViewSet.as_view({'get': 'list'}), name='contact-list'),
    path('footer-contacts/<int:pk>/', ContactViewSet.as_view({'get': 'retrieve'}), name='contact-detail'),
    path('footer-addresses/', AddressViewSet.as_view({'get': 'list'}), name='address-list'),
    path('footer-addresses/<int:pk>/', AddressViewSet.as_view({'get': 'retrieve'}), name='address-detail'),
    path('partners/', PartnerViewSet.as_view({'get': 'list'}), name='partner-list'),
    path('partners/<int:pk>/', PartnerViewSet.as_view({'get': 'retrieve'}), name='partner-detail'),
    path('about-us/', AboutUsViewSet.as_view({'get': 'list'}), name='about-us-list'),
    path('about-us/<int:pk>/', AboutUsViewSet.as_view({'get': 'retrieve'}), name='about-us-detail'),
    path('faqs/', FAQViewSet.as_view({'get': 'list'}), name='faq-list'),
    path('faqs/<int:pk>/', FAQViewSet.as_view({'get': 'retrieve'}), name='faq-detail'),
    path('boycott/', BoycottViewSet.as_view({'get': 'list'}), name='boycott-company-list'),
    path('boycott/<int:pk>/', BoycottViewSet.as_view({'get': 'retrieve'}), name='boycott-company-detail'),
    path('our-achievements/', OurAchievementViewSet.as_view({'get': 'list'}), name='our-achievements-list'),
    path('our-achievements/<int:pk>/', OurAchievementViewSet.as_view({'get': 'retrieve'}), name='our-achievements-detail'),
    path('goals-objectives/', OurGoalsAndObjectivesViewSet.as_view({'get': 'list'}), name='goals-objectives-list'),
    path('goals-objectives/<int:pk>/', OurGoalsAndObjectivesViewSet.as_view({'get': 'retrieve'}), name='goals-objectives-detail'),
    path('team/', OurTeamViewSet.as_view({'get': 'list'}), name='team-list'),
    path('team/<int:pk>/', OurTeamViewSet.as_view({'get': 'retrieve'}), name='team-detail'),
    path('our-achievement-certificates/', OurAchievementCertificateImageViewSet.as_view({'get': 'list'}), name='achievement-certificates-list'),
    path('our-achievement-certificates/<int:pk>/', OurAchievementCertificateImageViewSet.as_view({'get': 'retrieve'}), name='achievement-certificates-detail'),
    path('reviews/', ReviewViewSet.as_view({'get': 'list'}), name='reviews-list'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve'}), name='reviews-detail'),
    path('process-of-obtaining-certificate/', ProcessOfObtainingCertificateViewSet.as_view({'get': 'list'}), name='process-of-obtaining-certificate-list'),
    path('process-of-obtaining-certificate/<int:pk>/', ProcessOfObtainingCertificateViewSet.as_view({'get': 'retrieve'}), name='process-of-obtaining-certificate-detail'),
    path('our-indicators/', OurIndicatorsViewSet.as_view({'get': 'list'}), name='our-indicators-list'),
    path('our-indicators/<int:pk>/', OurIndicatorsViewSet.as_view({'get': 'retrieve'}), name='our-indicators-detail'),
    path('client/', ClientViewSet.as_view({'get': 'list'}), name='client-list'),
    path('client/<int:pk>/', ClientViewSet.as_view({'get': 'retrieve'}), name='client-detail'),
    path('ratings/', RatingViewSet.as_view({'get': 'list', 'post':'create'}), name='rating-list'),
    path('ratings/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve'}), name='rating-detail'),
    path('main-phone-number/', MainPhoneNumberViewSet.as_view({'get': 'list'}), name='main-phone-number-list'),
    path('main-phone-number/<int:pk>/', MainPhoneNumberViewSet.as_view({'get': 'retrieve'}), name='main-phone-number-detail'),
    path('footer-our-sites/', OurSitesViewSet.as_view({'get': 'list'}), name='our-sites-list'),
    path('footer-our-sites/<int:pk>/', OurSitesViewSet.as_view({'get': 'retrieve'}), name='our-sites-detail'),
    path('footer-social-network-sites/', SocialNetworkViewSet.as_view({'get': 'list'}), name='our-social-network-list'),
    path('footer-social-network-sites/<int:pk>/', SocialNetworkViewSet.as_view({'get': 'retrieve'}), name='our-social-network-detail'),
    path('mobile-app-url/', MobileAppUrlViewSet.as_view({'get': 'list'}), name='mobile-app-url-list'),
    path('mobile-app-url/<int:pk>/', MobileAppUrlViewSet.as_view({'get': 'retrieve'}), name='mobile-app-url-detail'),
    path('suggestions-or-complaints/', SuggestionsOrComplaintsViewSet.as_view({'get': 'list'}), name='suggestions-or-complaints-list'),
    path('suggestions-or-complaints/<int:pk>/', SuggestionsOrComplaintsViewSet.as_view({'get': 'retrieve'}), name='suggestions-or-complaints-detail'),
]

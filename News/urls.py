from django.urls import path
from .views import *


urlpatterns = [
    path('news/', NewsViewSets.as_view({'get': 'list'}), name='news-list'),
    path('news/<int:pk>/', NewsViewSets.as_view({'get': 'retrieve'}), name='news-detail'),
    path('news-photos/', NewsPhotoViewSets.as_view({'get': 'list'}), name='newsphoto-list'),
    path('news-photos/<int:pk>/', NewsPhotoViewSets.as_view({'get': 'retrieve'}), name='newsphoto-detail'),
    path('parse-youtube-videos/', adal_kg_parsing_videos, name='parse-youtube-videos'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('news/', NewsViewSets.as_view({'get': 'list'}), name='news-list'),
    path('newsphotos/', NewsPhotoViewSets.as_view({'get': 'list'}), name='newsphotos-list')
]
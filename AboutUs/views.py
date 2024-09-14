from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import *
from .models import *
import yt_dlp
from django.conf import settings


class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class LocateViewSet(viewsets.ModelViewSet):
    queryset = Locate.objects.all()
    serializer_class = LocateSerializer

class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

def tez_kaber_parsing_videos(request):
    channel_url = request.GET.get('channel_url', f'https://www.youtube.com/@{settings.YT_TEZ_KABAR_CHANNEL}/videos')
    
    if not isinstance(channel_url, str):
        return JsonResponse({'error': 'Invalid URL format'}, status=400)
    
    ydl_opts = {
        'quiet': True,
        'extract_flat': 'in_playlist',
        'playlist_items': '1-50',
        'skip_download': True,
        'force_generic_extractor': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(channel_url, download=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    data = []
    for entry in info_dict.get('entries', []):
        video_url = entry.get('url')
        video_title = entry.get('title')
        video_date = entry.get('upload_date')
        video_description = entry.get('description')
        video_image = entry.get('thumbnails')
        video_view_count = entry.get('view_count')
        data.append({
            "Название": video_title,
            "URL": video_url,
            "Описание": video_description,
            "Дата публикации": video_date,
            "Фото превью": video_image[2]['url'] if len(video_image) > 2 else None,
            "Просмотры": video_view_count,
        })

    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})

class BlackListCompaniesViewSet(viewsets.ModelViewSet):
    queryset = BlackListCompanies.objects.all()
    serializer_class = BlackListCompaniesSerializer

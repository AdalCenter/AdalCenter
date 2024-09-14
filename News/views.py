import yt_dlp
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import JsonResponse
from django.conf import settings


class NewsViewSets(ModelViewSet):
    queryset = News.objects.all().order_by('-date')  # Сортировка по дате (новости в порядке убывания)
    serializer_class = NewsSerializer
    parser_classes = [MultiPartParser, FormParser]

#    def retrieve(self, request, *args, **kwargs):
#        instance = self.get_object()
#        instance.view_count += 1
#        instance.save()
#        return super().retrieve(request, *args, **kwargs)

class NewsPhotoViewSets(ModelViewSet):
    queryset = NewsPhoto.objects.all()
    serializer_class = NewsPhotoSerializer
    parser_classes = [MultiPartParser, FormParser]

def adal_kg_parsing_videos(request):
    channel_url = request.GET.get('channel_url', f'https://www.youtube.com/@{settings.YT_ADAL_KG_CHANNEL}/videos')

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

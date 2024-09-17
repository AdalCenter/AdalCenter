import yt_dlp
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import JsonResponse
from django.conf import settings
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class NewsViewSets(ModelViewSet):
    """
    API для управления новостями.

    **GET /news/**: Получить список всех новостей.
    **GET /news/{id}/**: Получить детальную информацию о конкретной новости по идентификатору.
    """

    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Получить список всех новостей",
        operation_description="Этот эндпоинт возвращает список всех новостей.",
        responses={200: NewsSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        """
        Получить список всех новостей.
        """
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            raise APIException(f'Ошибка получения списка новостей: {str(e)}')

    @swagger_auto_schema(
        operation_summary="Получить детальную информацию о новости",
        operation_description="Этот эндпоинт возвращает детальную информацию о конкретной новости по идентификатору.",
        responses={
            200: NewsSerializer,
            404: openapi.Response('Новость не найдена')
        },
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Получить детальную информацию о конкретной новости.
        """
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception as e:
            raise APIException(f'Ошибка получения детали новости: {str(e)}')


class NewsPhotoViewSets(ModelViewSet):
    """
    API для управления фото новостей.

    **GET /news-photos/**: Получить список всех фото новостей.
    **GET /news-photos/{id}/**: Получить детальную информацию о конкретном фото новости.
    """

    queryset = NewsPhoto.objects.all()
    serializer_class = NewsPhotoSerializer
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Получить список всех фото новостей",
        operation_description="Этот эндпоинт возвращает список всех фото новостей.",
        responses={200: NewsPhotoSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        """
        Получить список всех фото новостей.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Получить детальную информацию о фото новости",
        operation_description="Этот эндпоинт возвращает детальную информацию о конкретном фото новости по идентификатору.",
        responses={
            200: NewsPhotoSerializer,
            404: openapi.Response('Фото не найдено')
        },
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Получить детальную информацию о конкретном фото новости.
        """
        return super().retrieve(request, *args, **kwargs)

@swagger_auto_schema(
    method='get',
    operation_summary="Получить список видео с YouTube канала",
    operation_description="Этот эндпоинт позволяет извлечь видео с указанного YouTube канала. Используйте параметр `channel_url` для указания канала.",
    manual_parameters=[
        openapi.Parameter('channel_url', openapi.IN_QUERY, description="URL канала YouTube", type=openapi.TYPE_STRING)
    ],
    responses={
        200: openapi.Response(
            'Список видео',
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'Название': openapi.Schema(type=openapi.TYPE_STRING),
                        'URL': openapi.Schema(type=openapi.TYPE_STRING),
                        'Описание': openapi.Schema(type=openapi.TYPE_STRING),
                        'Дата публикации': openapi.Schema(type=openapi.TYPE_STRING),
                        'Фото превью': openapi.Schema(type=openapi.TYPE_STRING),
                        'Просмотры': openapi.Schema(type=openapi.TYPE_INTEGER),
                    }
                )
            )
        ),
        400: openapi.Response('Неверный формат URL', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)})),
        500: openapi.Response('Ошибка при извлечении информации', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)})),
    },
)
@api_view(['GET'])
def adal_kg_parsing_videos(request):
    """
    Получить список видео с YouTube канала.

    **GET /parse-videos/?channel_url={url}**: Извлечь видео с указанного канала.
    """
    channel_url = request.GET.get('channel_url', f'https://www.youtube.com/@{settings.YT_ADAL_KG_CHANNEL}/videos')

    if not isinstance(channel_url, str):
        return JsonResponse({'error': 'Неверный формат URL'}, status=400)

    ydl_opts = {
        'quiet': True,
        'extract_flat': 'in_playlist',
        'playlist_items': '1-50',
        'skip_download': True,
        'force_generic_extractor': True,
        'http_headers': {
            'User-Agent': 'Your Custom User Agent String',
        },
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(channel_url, download=False)
    except Exception as e:
        return JsonResponse({'error': f'Ошибка при извлечении информации: {str(e)}'}, status=500)

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

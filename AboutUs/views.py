from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .serializers import *
from .models import *
import yt_dlp
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view


class ContactViewSet(viewsets.ModelViewSet):
    """
    API для управления контактами.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @swagger_auto_schema(
        operation_summary="Получить список контактов",
        responses={
            200: openapi.Response("Успешный ответ", ContactSerializer(many=True)),
            404: "Контакты не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения контактов'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить контакт по ID",
        responses={
            200: openapi.Response("Успешный ответ", ContactSerializer()),
            404: "Контакт не найден"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения контакта'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddressViewSet(viewsets.ModelViewSet):
    """
    API для управления адресами.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @swagger_auto_schema(
        operation_summary="Получить список адресов",
        responses={
            200: openapi.Response("Успешный ответ", AddressSerializer(many=True)),
            404: "Адреса не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения адресов'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить адрес по ID",
        responses={
            200: openapi.Response("Успешный ответ", AddressSerializer()),
            404: "Адрес не найден"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения адреса'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PartnerViewSet(viewsets.ModelViewSet):
    """
    API для управления партнерами.
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    @swagger_auto_schema(
        operation_summary="Получить список партнеров",
        responses={
            200: openapi.Response("Успешный ответ", PartnerSerializer(many=True)),
            404: "Партнеры не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения партнеров'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить партнера по ID",
        responses={
            200: openapi.Response("Успешный ответ", PartnerSerializer()),
            404: "Партнер не найден"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения партнера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AboutUsViewSet(viewsets.ModelViewSet):
    """
    API для управления информацией 'О нас'.
    """
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    @swagger_auto_schema(
        operation_summary="Получить информацию 'О нас'",
        responses={
            200: openapi.Response("Успешный ответ", AboutUsSerializer(many=True)),
            404: "Информация не найдена"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения информации "О нас"'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить информацию 'О нас' по ID",
        responses={
            200: openapi.Response("Успешный ответ", AboutUsSerializer()),
            404: "Информация не найдена"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения информации "О нас"'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FAQViewSet(viewsets.ModelViewSet):
    """
    API для управления часто задаваемыми вопросами.
    """
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    @swagger_auto_schema(
        operation_summary="Получить список часто задаваемых вопросов",
        responses={
            200: openapi.Response("Успешный ответ", FAQSerializer(many=True)),
            404: "Вопросы не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения вопросов'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить вопрос по ID",
        responses={
            200: openapi.Response("Успешный ответ", FAQSerializer()),
            404: "Вопрос не найден"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения вопроса'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BlackListCompanyViewSet(viewsets.ModelViewSet):
    """
    API для управления черным списком компаний.
    """
    queryset = BlackListCompany.objects.all()
    serializer_class = BlackListCompanySerializer

    @swagger_auto_schema(
        operation_summary="Получить список черного списка компаний",
        responses={
            200: openapi.Response("Успешный ответ", BlackListCompanySerializer(many=True)),
            404: "Компании не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения компаний из черного списка'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить компанию из черного списка по ID",
        responses={
            200: openapi.Response("Успешный ответ", BlackListCompanySerializer()),
            404: "Компания не найдена"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения компании из черного списка'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OurAchievementViewSet(viewsets.ModelViewSet):
    """
    API для управления достижениями.
    """
    queryset = OurAchievement.objects.all()
    serializer_class = OurAchievementSerializer

    @swagger_auto_schema(
        operation_summary="Получить список достижений",
        responses={
            200: openapi.Response("Успешный ответ", OurAchievementSerializer(many=True)),
            404: "Достижения не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения достижений'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить достижение по ID",
        responses={
            200: openapi.Response("Успешный ответ", OurAchievementSerializer()),
            404: "Достижение не найдено"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения достижения'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OurGoalsAndObjectivesViewSet(viewsets.ModelViewSet):
    """
    API для управления целями и задачами.
    """
    queryset = OurGoalsAndObjectives.objects.all()
    serializer_class = OurGoalsAndObjectivesSerializer

    @swagger_auto_schema(
        operation_summary="Получить список целей и задач",
        responses={
            200: openapi.Response("Успешный ответ", OurGoalsAndObjectivesSerializer(many=True)),
            404: "Цели и задачи не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения целей и задач'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить цель или задачу по ID",
        responses={
            200: openapi.Response("Успешный ответ", OurGoalsAndObjectivesSerializer()),
            404: "Цель или задача не найдена"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения цели или задачи'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OurTeamViewSet(viewsets.ModelViewSet):
    """
    API для управления информацией о команде.
    """
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer

    @swagger_auto_schema(
        operation_summary="Получить список членов команды",
        responses={
            200: openapi.Response("Успешный ответ", OurTeamSerializer(many=True)),
            404: "Члены команды не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения членов команды'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить члена команды по ID",
        responses={
            200: openapi.Response("Успешный ответ", OurTeamSerializer()),
            404: "Член команды не найден"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения члена команды'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OurAchievementCertificateImageViewSet(viewsets.ModelViewSet):
    """
    API для управления изображениями сертификатов достижений.
    """
    queryset = OurAchievementCertificateImage.objects.all()
    serializer_class = OurAchievementCertificateImageSerializer

    @swagger_auto_schema(
        operation_summary="Получить список изображений сертификатов",
        responses={
            200: openapi.Response("Успешный ответ", OurAchievementCertificateImageSerializer(many=True)),
            404: "Изображения не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения изображений сертификатов'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить изображение сертификата по ID",
        responses={
            200: openapi.Response("Успешный ответ", OurAchievementCertificateImageSerializer()),
            404: "Изображение не найдено"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения изображения сертификата'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API для управления изображениями сертификатов достижений.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @swagger_auto_schema(
        operation_summary="Получить список отзывов",
        responses={
            200: openapi.Response("Успешный ответ", ReviewSerializer(many=True)),
            404: "Отзывы не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения отзывов'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить отзыв по ID",
        responses={
            200: openapi.Response("Успешный ответ", ReviewSerializer()),
            404: "Отзыв не найдено"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения отзыва'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(
    method='get',
    operation_summary="Парсинг видео с канала Tez Kabar",
    operation_description="Этот эндпоинт позволяет извлечь видео с указанного YouTube канала Tez Kabar. Используйте параметр `channel_url` для указания канала.",
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
        404: openapi.Response('Видео не найдены', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)})),
        500: openapi.Response('Ошибка при извлечении информации', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)})),
    },
)
@api_view(['GET'])
def tez_kabar_parsing_videos(request):
    """
    Парсинг видео с канала Tez Kabar.
    """
    channel_url = request.GET.get('channel_url', f'https://www.youtube.com/@{settings.YT_TEZ_KABAR_CHANNEL}/videos')
    
    if not isinstance(channel_url, str):
        return JsonResponse({'error': 'Неверный формат URL'}, status=400)
    
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

    if not info_dict.get('entries'):
        return JsonResponse({'error': 'Видео не найдены'}, status=404)

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

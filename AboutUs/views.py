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
    API для управления контактами (Футер).
    """
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer

    @swagger_auto_schema(
        operation_summary="Получить список контактов (Футер)",
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
        operation_summary="Получить контакт по ID (Футер)",
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
    API для управления адресами (Футер).
    """
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer

    @swagger_auto_schema(
        operation_summary="Получить список адресов (Футер)",
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
        operation_summary="Получить адрес по ID (Футер)",
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
    queryset = Partner.objects.all().order_by('id')
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
    queryset = AboutUs.objects.all().order_by('id')
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

class BoycottViewSet(viewsets.ModelViewSet):
    """
    API для управления черным списком компаний.
    """
    queryset = Boycott.objects.all().order_by('id')
    serializer_class = BoycottSerializer

    @swagger_auto_schema(
        operation_summary="Получить список черного списка компаний",
        responses={
            200: openapi.Response("Успешный ответ", BoycottSerializer(many=True)),
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
            200: openapi.Response("Успешный ответ", BoycottSerializer()),
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
    queryset = OurAchievement.objects.all().order_by('id')
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
    queryset = OurGoalsAndObjectives.objects.all().order_by('id')
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
    queryset = OurTeam.objects.all().order_by('id')
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
    queryset = OurAchievementCertificateImage.objects.all().order_by('id')
    serializer_class = OurAchievementCertificateImageSerializer

    @swagger_auto_schema(
        operation_summary="Получить список изображений наших сертификатов",
        responses={
            200: openapi.Response("Успешный ответ", OurAchievementCertificateImageSerializer(many=True)),
            404: "Изображения не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения изображений наших сертификатов'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
            return Response({'error': 'Ошибка получения изображения наших сертификата'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API для управления изображениями сертификатов достижений.
    """
    queryset = Review.objects.all().order_by('id')
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
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        },
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

class ProcessOfObtainingCertificateViewSet(viewsets.ModelViewSet):
    """
    API для управления процессом получения сертификата.
    """
    queryset = ProcessOfObtainingCertificate.objects.all().order_by('id')
    serializer_class = ProcessOfObtainingCertificateSerializer

    @swagger_auto_schema(
        operation_summary="Получить список этапов получения сертификата",
        responses={
            200: openapi.Response("Успешный ответ", ProcessOfObtainingCertificateSerializer(many=True)),
            404: "Этап получения сертификата не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения этапов получения сертификата'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить этап получения сертификата по ID",
        responses={
            200: openapi.Response("Успешный ответ", ProcessOfObtainingCertificateSerializer()),
            404: "Этап получения сертификата не найдено"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения этапа получения сертификата'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OurIndicatorsViewSet(viewsets.ModelViewSet):
    """
    API для управления показателями.
    """
    queryset = OurIndicators.objects.all().order_by('id')
    serializer_class = OurIndicatorsSerializer

    @swagger_auto_schema(
        operation_summary="Получить список показателей",
        responses={
            200: openapi.Response("Успешный ответ", OurIndicatorsSerializer(many=True)),
            404: "Показатель не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения показателей'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить показатель по ID",
        responses={
            200: openapi.Response("Успешный ответ", OurIndicatorsSerializer()),
            404: "Показатель не найдено"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения показателя'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ClientViewSet(viewsets.ModelViewSet):
    """
    API для управления клиентами.
    """
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer

    @swagger_auto_schema(
        operation_summary="Получить список клиентов",
        responses={
            200: openapi.Response("Успешный ответ", ClientSerializer(many=True)),
            404: "Клиент не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения клиентов'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить клиента по ID",
        responses={
            200: openapi.Response("Успешный ответ", ClientSerializer()),
            404: "Клиент не найден"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения клиента'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RatingViewSet(viewsets.ModelViewSet):
    """
    API для управления рейтингами и источниками информации о сайте.
    """
    queryset = RatingAndHowYouHeardAboutOurSite.objects.all().order_by('id')
    serializer_class = RatingSerializer

    @swagger_auto_schema(
        operation_summary="Создать новый рейтинг",
        request_body=RatingSerializer,
        responses={
            201: openapi.Response("Успешно создано", RatingSerializer()),
            400: "Некорректные данные",
            500: "Ошибка сервера"
        }
    )
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка создания рейтинга'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить список рейтингов",
        responses={
            200: openapi.Response("Успешный ответ", RatingSerializer(many=True)),
            404: "Рейтинги не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения рейтингов'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить рейтинг по ID",
        responses={
            200: openapi.Response("Успешный ответ", RatingSerializer()),
            404: "Рейтинг не найден"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения рейтинга'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MainPhoneNumberViewSet(viewsets.ModelViewSet):
    """
    API для управления Номером в главном меню.
    """
    queryset = MainPhoneNumber.objects.all().order_by('id')
    serializer_class = MainPhoneNumberSerializer

    @swagger_auto_schema(
        operation_summary="Получить список номеров в главном меню",
        responses={
            200: openapi.Response("Успешный ответ", MainPhoneNumberSerializer(many=True)),
            404: "Номера не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения номеров'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить номер по ID",
        responses={
            200: openapi.Response("Успешный ответ", MainPhoneNumberSerializer()),
            404: "Номер не найден"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения номера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OurSitesViewSet(viewsets.ModelViewSet):
    """
    API для управления сайтом.
    """
    queryset = OurSites.objects.all().order_by('id')
    serializer_class = OurSitesSerializer

    @swagger_auto_schema(
        operation_summary="Получить список сайтов",
        responses={
            200: openapi.Response("Успешный ответ", OurSitesSerializer(many=True)),
            404: "Сайты не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения сайтов'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить сайт по ID",
        responses={
            200: openapi.Response("Успешный ответ", OurSitesSerializer()),
            404: "Сайт не найден"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения сайта'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SocialNetworkViewSet(viewsets.ModelViewSet):
    """
    API для управления социальной сети.
    """
    queryset = SocialNetwork.objects.all().order_by('id')
    serializer_class = SocialNetworkSerializer

    @swagger_auto_schema(
        operation_summary="Получить список социальных сетей",
        responses={
            200: openapi.Response("Успешный ответ", SocialNetworkSerializer(many=True)),
            404: "Социальные сети не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения социальных сетей'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить социальную сеть по ID",
        responses={
            200: openapi.Response("Успешный ответ", SocialNetworkSerializer()),
            404: "Социальная сеть не найдена"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения социальной сети'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MobileAppUrlViewSet(viewsets.ModelViewSet):
    """
    API для управления ссылками на мобильное приложение.
    """
    queryset = MobileAppUrl.objects.all().order_by('id')
    serializer_class = MobileAppUrlSerializer

    @swagger_auto_schema(
        operation_summary="Получить список ссылок на мобильное приложение",
        responses={
            200: openapi.Response("Успешный ответ", MobileAppUrlSerializer(many=True)),
            404: "Ссылки на мобильное приложение не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения ссылок на мобильное приложение'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить ссылки на мобильное приложение по ID",
        responses={
            200: openapi.Response("Успешный ответ", MobileAppUrlSerializer()),
            404: "Ссылки на мобильное приложениене найдена"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения ссылки на мобильное приложение'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SuggestionsOrComplaintsViewSet(viewsets.ModelViewSet):
    """
    API для управления ссылками на WhatsApp и Telegram для жалоб и предложений.
    """
    queryset = SuggestionsOrComplaints.objects.all().order_by('id')
    serializer_class = SuggestionsOrComplaintsSerializer

    @swagger_auto_schema(
        operation_summary="Получить список ссылок на WhatsApp и Telegram для жалоб и предложений",
        responses={
            200: openapi.Response("Успешный ответ", SuggestionsOrComplaintsSerializer(many=True)),
            404: "Ссылки на WhatsApp и Telegram для жалоб и предложений не найдены"
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения ссылок на WhatsApp и Telegram для жалоб и предложений'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Получить ссылки на WhatsApp и Telegram для жалоб и предложений по ID",
        responses={
            200: openapi.Response("Успешный ответ", SuggestionsOrComplaintsSerializer()),
            404: "WhatsApp и Telegram для жалоб и предложений найдена"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception:
            return Response({'error': 'Ошибка получения ссылки на WhatsApp и Telegram для жалоб и предложений'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework import exceptions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CertifiedCompanyFilter
import os
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
from django.utils.encoding import smart_str
from rest_framework.decorators import api_view


class ObserverViewSet(viewsets.ModelViewSet):
    """
    API endpoint для управления наблюдателями.
    """
    queryset = Observer.objects.all().order_by('id')
    serializer_class = ObserverSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Получить список наблюдателей",
        operation_description="Этот эндпоинт позволяет получить список всех наблюдателей.",
        responses={200: ObserverSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Получить информацию о наблюдателе",
        operation_description="Этот эндпоинт позволяет получить информацию о конкретном наблюдателе по его ID.",
        responses={
            200: ObserverSerializer,
            404: openapi.Response('Наблюдатель не найден')
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def handle_exception(self, exc):
        if isinstance(exc, exceptions.NotFound):
            return Response({'error': 'Наблюдатель не найден'}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint для управления сервисами.
    """
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Получить список сервисов",
        operation_description="Этот эндпоинт позволяет получить список всех сервисов.",
        responses={200: ServiceSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Получить информацию о сервисе",
        operation_description="Этот эндпоинт позволяет получить информацию о конкретном сервисе по его ID.",
        responses={
            200: ServiceSerializer,
            404: openapi.Response('Сервис не найден')
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def handle_exception(self, exc):
        if isinstance(exc, exceptions.NotFound):
            return Response({'error': 'Сервис не найден'}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)

class CertifiedCompanyListViewSet(viewsets.ModelViewSet):
    """
    API endpoint для управления сертифицированными компаниями.
    """
    queryset = CertifiedCompany.objects.all().order_by('id')
    serializer_class = CertifiedCompanyListSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = CertifiedCompanyFilter

    @swagger_auto_schema(
        operation_summary="Получить список сертифицированных компаний",
        operation_description="Этот эндпоинт позволяет получить список всех сертифицированных компаний.",
        responses={200: CertifiedCompanyListSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Получить информацию о компании",
        operation_description="Этот эндпоинт позволяет получить информацию о конкретной сертифицированной компании по ее ID.",
        responses={
            200: CertifiedCompanyListSerializer,
            404: openapi.Response('Компания не найдена')
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def handle_exception(self, exc):
        if isinstance(exc, exceptions.NotFound):
            return Response({'error': 'Компания не найдена'}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)

@api_view(['GET'])
def download_certificate(request, filename):
    certificate_dir = os.path.join(settings.MEDIA_ROOT, 'certificate_photos')
    file_path = os.path.join(certificate_dir, filename)

    if os.path.exists(file_path) and os.path.commonprefix([file_path, certificate_dir]) == certificate_dir:
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename={smart_str(filename)}'
            return response
    else:
        raise Http404("Файл не найден или доступ к нему запрещен.")

@swagger_auto_schema(
    method='get',
    operation_description="Получить список доступных фильтров для сертифицированных компаний. "
                          "Этот API возвращает возможные значения для фильтрации компаний по регионам, "
                          "типам услуг, типам сертификатов и наблюдателям.",
    responses={
        200: openapi.Response(
            description="Успешный ответ с вариантами фильтров",
            examples={
                "application/json": {
                    "regions": ["Ошская область", "Чуйская область"],
                    "service_types": ["BBQ", "Type 1", "Type 2"],
                    "certificate_types": ["Сертифицированный", "В процессе", "Истекшие"],
                    "observer": ["Иван Иванов", "Петр Петров"]
                }
            }
        )
    },
    manual_parameters=[
        openapi.Parameter(
            'detail', openapi.IN_QUERY, 
            description="Флаг для вывода детальной информации (true/false). "
                        "Если true, добавляется дополнительная информация о каждом фильтре.",
            type=openapi.TYPE_BOOLEAN
        )
    ]
)
@api_view(['GET'])
def get_filter_options(request):
    """
    Получить список доступных вариантов фильтров для сертифицированных компаний:
    
    - **regions**: регионы, в которых зарегистрированы компании.
    - **service_types**: типы услуг, которые предоставляют компании.
    - **certificate_types**: статусы сертификатов компаний (например, 'Сертифицированный', 'Истекшие').
    - **observer**: список наблюдателей, ассоциированных с компаниями.

    Этот эндпоинт помогает в фильтрации данных по вышеуказанным критериям.
    """
    regions = CertifiedCompany.objects.values_list('region', flat=True).distinct()
    service_types = CertifiedCompany.objects.values_list('service_type__service', flat=True).distinct()
    certificate_types = CertifiedCompany.objects.values_list('certificate_type', flat=True).distinct()
    observer = CertifiedCompany.objects.values_list('observer__fullname', flat=True).distinct()

    if request.GET.get('detail') == 'true':
        detailed_info = {
            "regions_description": "Это список всех регионов, где зарегистрированы сертифицированные компании.",
            "service_types_description": "Это возможные типы услуг, которые предоставляют сертифицированные компании.",
            "certificate_types_description": "Это типы сертификатов, которые имеют компании, включая истекшие, активные и процесс получения."
        }
        return JsonResponse({
            "regions": list(regions),
            "service_types": list(service_types),
            "certificate_types": list(certificate_types),
            "observer": list(observer),
            "details": detailed_info
        })

    return JsonResponse({
        "regions": list(regions),
        "service_types": list(service_types),
        "certificate_types": list(certificate_types),
        "observer": list(observer)
    })

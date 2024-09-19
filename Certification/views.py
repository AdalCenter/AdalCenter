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
from rest_framework import filters as drf_filters
from .filters import CertifiedCompanyFilter


class ObserverViewSet(viewsets.ModelViewSet):
    """
    API endpoint для управления наблюдателями.
    """
    queryset = Observer.objects.all()
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
    queryset = Service.objects.all()
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
    queryset = CertifiedCompany.objects.all()
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

import os
from django.http import HttpResponse, Http404
from django.conf import settings
from django.utils.encoding import smart_str
from rest_framework.decorators import api_view

@api_view(['GET'])
def download_certificate(request, filename):
    # Путь к директории, где хранятся файлы сертификатов
    file_path = os.path.join(settings.MEDIA_ROOT, 'company_photos', filename)
    
    # Проверка, существует ли файл
    if os.path.exists(file_path):
        # Открываем файл для чтения в бинарном режиме
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/force-download')
            # Добавляем заголовок для загрузки файла
            response['Content-Disposition'] = f'attachment; filename={smart_str(filename)}'
            return response
    else:
        # Если файл не найден, возвращаем 404 ошибку
        raise Http404("Файл не найден")


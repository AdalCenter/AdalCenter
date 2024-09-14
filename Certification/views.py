from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework import exceptions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ObserverViewSet(viewsets.ModelViewSet):
    """
    API endpoint для управления наблюдателями.
    """
    queryset = Observer.objects.all()
    serializer_class = ObserverSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получение списка наблюдателей.",
        responses={200: ObserverSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение информации о конкретном наблюдателе.",
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
        operation_description="Получение списка сервисов.",
        responses={200: ServiceSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение информации о конкретном сервисе.",
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

    @swagger_auto_schema(
        operation_description="Получение списка сертифицированных компаний.",
        responses={200: CertifiedCompanyListSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение информации о конкретной сертифицированной компании.",
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

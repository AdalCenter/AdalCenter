from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .filters import *
from .models import *
from drf_yasg.utils import swagger_auto_schema


class ProductBarCodeViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с штрих-кодами продуктов.
    """
    queryset = ProductBarCode.objects.all()
    serializer_class = ProductBarCodeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductBarCodeFilter

    @swagger_auto_schema(
        operation_description="Получить список всех штрих-кодов продуктов.",
        responses={200: ProductBarCodeSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        """
        Получить список всех штрих-кодов продуктов.
        """
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Получить детали конкретного штрих-кода продукта.",
        responses={
            200: ProductBarCodeSerializer,
            404: "Штрих-код не найден",
        },
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Получить детали конкретного штрих-кода продукта.
        """
        try:
            return super().retrieve(request, *args, **kwargs)
        except ProductBarCode.DoesNotExist:
            return Response({'error': 'Штрих-код не найден'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

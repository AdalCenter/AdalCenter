from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ECode
from .serializers import ECodeSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ECodeViewSet(viewsets.ModelViewSet):
    """
    API для управления Е-кодами.
    """
    queryset = ECode.objects.all().order_by('id')
    serializer_class = ECodeSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить список всех Е-кодов.",
        responses={200: ECodeSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Получить детальную информацию о конкретном Е-коде.",
        responses={
            200: ECodeSerializer,
            404: openapi.Response("Е-код не найден.")
        }
    )
    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except ECode.DoesNotExist:
            return Response({"detail": "Е-код не найден."}, status=status.HTTP_404_NOT_FOUND)

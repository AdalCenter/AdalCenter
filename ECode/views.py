from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ECode, CodeType, TypeOfOrigin
from .serializers import ECodeSerializer, CodeTypeSerializer, TypeOfOriginSerializer
from rest_framework.permissions import AllowAny

class ECodeViewSet(viewsets.ModelViewSet):
    """
    API для управления Е-кодами.
    """
    queryset = ECode.objects.all()
    serializer_class = ECodeSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

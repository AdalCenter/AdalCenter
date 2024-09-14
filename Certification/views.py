from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny


class ObserverViewSet(viewsets.ModelViewSet):
    queryset = Observer.objects.all()
    serializer_class = ObserverSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CertifiedCompanySerializer
        return super().get_serializer_class()

class CertifiedCompanyListViewSet(viewsets.ModelViewSet):
    queryset = CertifiedCompany.objects.all()
    serializer_class = CertifiedCompanyListSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

class CertifiedCompanyDetailView(generics.RetrieveAPIView):
    queryset = CertifiedCompany.objects.all()
    serializer_class = CertifiedCompanySerializer
    parser_classes = [MultiPartParser, FormParser]

class ServiceCompaniesView(generics.GenericAPIView):
    serializer_class = CertifiedCompanyListSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            return CertifiedCompany.objects.none()

        try:
            service = Service.objects.get(pk=pk)
            return service.companies.all()
        except Service.DoesNotExist:
            return CertifiedCompany.objects.none()

    def get(self, request, pk, *args, **kwargs):
        companies = self.get_queryset()
        if not companies.exists():
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(companies, many=True)
        return Response(serializer.data)

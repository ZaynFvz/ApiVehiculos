from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Vehiculo, VehiculoDocumento
from .serializers import VehiculoSerializer, VehiculoDocumentoSerializer

class TblVehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class TblVehiculoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = VehiculoDocumento.objects.all()
    serializer_class = VehiculoDocumentoSerializer

from django.urls import path, include
from rest_framework import routers
from .views import TblVehiculoViewSet, TblVehiculoDocumentoViewSet

router = routers.DefaultRouter()
router.register('vehiculos', TblVehiculoViewSet)
router.register('documentos', TblVehiculoDocumentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

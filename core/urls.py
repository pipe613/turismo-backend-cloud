from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, DisponibilidadViewSet, ReservaViewSet, UserViewSet

router = DefaultRouter()
router.register(r'tours', TourViewSet)
router.register(r'disponibilidad', DisponibilidadViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'usuarios', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
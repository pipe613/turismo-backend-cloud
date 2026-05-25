from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, DisponibilidadViewSet, ReservaViewSet, UserViewSet, admin_panel

router = DefaultRouter()
router.register(r'tours', TourViewSet)
router.register(r'disponibilidad', DisponibilidadViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'usuarios', UserViewSet)

urlpatterns = [
    # Rutas de tu API
    path('', include(router.urls)),
    
    # Nueva ruta para tu panel de administración profesional
    path('admin-panel/', admin_panel, name='admin_panel'),
]
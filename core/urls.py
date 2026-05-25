from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, DisponibilidadViewSet, ReservaViewSet, UserViewSet, admin_panel, eliminar_tour, editar_tour

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
    path('admin-panel/editar/<int:tour_id>/', editar_tour, name='editar_tour'),
path('admin-panel/eliminar/<int:tour_id>/', eliminar_tour, name='eliminar_tour'),
]
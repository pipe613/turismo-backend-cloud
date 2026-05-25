from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .models import Tour, Disponibilidad, Reserva
from .serializers import (
    TourSerializer, 
    DisponibilidadSerializer, 
    ReservaSerializer, 
    UserSerializer
)

# --- 1. PANEL DE ADMINISTRACIÓN PROPIO ---
def admin_only(user):
    return user.is_staff

@login_required
@user_passes_test(admin_only)
def admin_panel(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        destino = request.POST.get('destino')
        precio = request.POST.get('precio')
        if nombre and destino and precio:
            Tour.objects.create(nombre=nombre, destino=destino, precio=precio)
            return redirect('admin_panel')
            
    tours = Tour.objects.all().order_by('-id')
    return render(request, 'admin_panel.html', {
        'tours': tours,
        'total_tours': tours.count(),
        'total_reservas': Reserva.objects.count(),
    })
    
@login_required
@user_passes_test(admin_only)
def eliminar_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    tour.delete()
    return redirect('admin_panel')

@login_required
@user_passes_test(admin_only)
def editar_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        tour.nombre = request.POST.get('nombre')
        tour.destino = request.POST.get('destino')
        tour.precio = request.POST.get('precio')
        tour.save()
        return redirect('admin_panel')
    return render(request, 'editar_tour.html', {'tour': tour})

# --- 2. API VIEWS (¡Necesarias para que la app móvil funcione!) ---
class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class DisponibilidadViewSet(viewsets.ModelViewSet):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
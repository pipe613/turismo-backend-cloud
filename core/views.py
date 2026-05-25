from rest_framework import viewsets
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tour, Disponibilidad, Reserva
from .serializers import (
    TourSerializer, 
    DisponibilidadSerializer, 
    ReservaSerializer, 
    UserSerializer
)

# --- PANEL DE ADMINISTRACIÓN PROPIO ---
@login_required
def admin_panel(request):
    # Lógica para mostrar y crear tours en nuestro panel limpio
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        destino = request.POST.get('destino')
        precio = request.POST.get('precio')
        if nombre and destino and precio:
            Tour.objects.create(nombre=nombre, destino=destino, precio=precio)
            return redirect('admin_panel')
            
    tours = Tour.objects.all()
    return render(request, 'admin_panel.html', {'tours': tours})

# --- API VIEWS ---
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
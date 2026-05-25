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

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Tour, Reserva

# Esta función verifica que el usuario sea administrador (Staff)
def admin_only(user):
    return user.is_staff

@login_required
@user_passes_test(admin_only) # ¡Seguridad reforzada!
def admin_panel(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        destino = request.POST.get('destino')
        precio = request.POST.get('precio')
        if nombre and destino and precio:
            Tour.objects.create(nombre=nombre, destino=destino, precio=precio)
            return redirect('admin_panel')
            
    # Estadísticas para el Dashboard
    tours = Tour.objects.all().order_by('-id')
    total_tours = tours.count()
    total_reservas = Reserva.objects.count()
    
    context = {
        'tours': tours,
        'total_tours': total_tours,
        'total_reservas': total_reservas,
    }
    return render(request, 'admin_panel.html', context)

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
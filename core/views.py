from django.shortcuts import render
from rest_framework import viewsets
from .models import Tour, Disponibilidad, Reserva
from django.contrib.auth.models import User
from .serializers import TourSerializer, DisponibilidadSerializer, ReservaSerializer, UserSerializer
from .models import Tour, Reserva 
from .serializers import TourSerializer, ReservaSerializer 


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class DisponibilidadViewSet(viewsets.ModelViewSet):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
from rest_framework import serializers
from .models import Tour, Disponibilidad, Reserva
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class DisponibilidadSerializer(serializers.ModelSerializer):
    tour_nombre = serializers.ReadOnlyField(source='tour.nombre')
    class Meta:
        model = Disponibilidad
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        # Excluimos 'usuario' y 'estado' porque los manejaremos en el ViewSet/Modelo
        fields = ['tour', 'fecha', 'cantidad_pasajeros', 'precio_total']
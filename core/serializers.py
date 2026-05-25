from rest_framework import serializers
from .models import Tour, Disponibilidad, Reserva
from django.contrib.auth.models import User
from .models import Tour, Reserva 


class ReservaSerializer(serializers.ModelSerializer):
    # Esto permite que el serializer acepte 'fecha' desde Flutter 
    # y la asigne internamente a 'fecha_reserva'
    fecha = serializers.DateField(source='fecha_reserva', write_only=True, required=False)

    class Meta:
        model = Reserva
        fields = ['id', 'user', 'tour', 'fecha_reserva', 'fecha']
        extra_kwargs = {
            'fecha_reserva': {'required': False} # Permite que sea opcional en la validación inicial
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class DisponibilidadSerializer(serializers.ModelSerializer):
    tour_nombre = serializers.ReadOnlyField(source='tour.nombre')

    class Meta:
        model = Disponibilidad
        fields = '__all__'
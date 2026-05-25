from rest_framework import serializers
from .models import Tour, Disponibilidad, Reserva
from django.contrib.auth.models import User
from .models import Tour, Reserva 


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

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
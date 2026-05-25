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
    # Aceptamos 'fecha' desde la App y lo mapeamos a 'fecha_reserva'
    fecha = serializers.DateField(source='fecha_reserva', write_only=True, required=True)

    class Meta:
        model = Reserva
        fields = ['id', 'user', 'tour', 'fecha_reserva', 'fecha']
        extra_kwargs = {
            'fecha_reserva': {'read_only': True},
            'user': {'required': False}
        }
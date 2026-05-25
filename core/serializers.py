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
    # Definimos 'fecha' como un campo extra que mapea a 'fecha_reserva'
    fecha = serializers.DateField(source='fecha_reserva', write_only=True, required=False)

    class Meta:
        model = Reserva
        fields = ['id', 'user', 'tour', 'fecha_reserva', 'fecha']
        # Hacemos que fecha_reserva no sea obligatorio en la validación inicial
        extra_kwargs = {
            'fecha_reserva': {'required': False},
            'user': {'required': False}
        }

    def validate(self, data):
        # Si la app envía 'fecha_reserva', la usamos. Si no, usamos 'fecha'.
        if not data.get('fecha_reserva') and data.get('fecha'):
            data['fecha_reserva'] = data['fecha']
        
        if not data.get('fecha_reserva'):
            raise serializers.ValidationError({"fecha": "Este campo es requerido."})
            
        return data
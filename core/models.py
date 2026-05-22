from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tour(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    destino = models.CharField(max_length=100)
    duracion_dias = models.PositiveIntegerField(help_text="Duración del tour en días")
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Disponibilidad(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='disponibilidades')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupos_totales = models.PositiveIntegerField()
    cupos_disponibles = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Disponibilidades"

    def __str__(self):
        return f"{self.tour.nombre} ({self.fecha_inicio} al {self.fecha_fin})"

class Reserva(models.Model):
    ESTADOS = [
        ('PE', 'Pendiente'),
        ('CO', 'Confirmada'),
        ('CA', 'Cancelada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    disponibilidad = models.ForeignKey(Disponibilidad, on_delete=models.PROTECT, related_name='reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='PE')
    cantidad_pasajeros = models.PositiveIntegerField(default=1)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reserva #{self.id} de {self.usuario.username}"
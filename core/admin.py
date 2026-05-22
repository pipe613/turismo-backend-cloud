from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tour, Disponibilidad, Reserva

admin.site.register(Tour)
admin.site.register(Disponibilidad)
admin.site.register(Reserva)
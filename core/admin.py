from django.contrib import admin
from .models import Tour, Reserva

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    # Columnas que se verán en la tabla principal
    list_display = ('nombre', 'destino', 'precio')
    # Agrega una barra de búsqueda
    search_fields = ('nombre', 'destino')
    # Agrega un panel de filtros lateral
    list_filter = ('destino',)
    # Ordena por precio de menor a mayor
    ordering = ('precio',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('tour', 'fecha', 'fecha_creacion')
    list_filter = ('fecha', 'tour')
    date_hierarchy = 'fecha' # Agrega un menú de navegación por fechas muy pro
from django.contrib import admin
from .models import Pelicula

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'año', 'director', 'duracion', 'clasificacion', 'calificacion_promedio']
    search_fields = ['titulo', 'titulo_original', 'sinopsis']
    list_filter = ['año', 'generos', 'clasificacion', 'pais']
    filter_horizontal = ['generos', 'actores']
    date_hierarchy = 'fecha_estreno'
    readonly_fields = ['fecha_agregada', 'actualizada']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'titulo_original', 'sinopsis', 'año', 'duracion')
        }),
        ('Equipo Creativo', {
            'fields': ('director', 'actores')
        }),
        ('Clasificación', {
            'fields': ('generos', 'clasificacion')
        }),
        ('Detalles de Producción', {
            'fields': ('pais', 'idioma', 'fecha_estreno', 'presupuesto', 'recaudacion')
        }),
        ('Multimedia', {
            'fields': ('poster', 'trailer')
        }),
        ('Metadatos', {
            'fields': ('fecha_agregada', 'actualizada'),
            'classes': ('collapse',)
        }),
    )
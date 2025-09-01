from django.contrib import admin
from .models import Programa, Curso, Estudiante, Inscripcion


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Programa.
    """
    list_display = ('codigo', 'nombre', 'duracion_semestres', 'activo', 'fecha_creacion')
    list_filter = ('activo', 'duracion_semestres', 'fecha_creacion')
    search_fields = ('nombre', 'codigo', 'descripcion')
    readonly_fields = ('fecha_creacion',)
    list_editable = ('activo',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'codigo', 'duracion_semestres', 'activo')
        }),
        ('Descripción', {
            'fields': ('descripcion',)
        }),
        ('Información del Sistema', {
            'fields': ('fecha_creacion',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Curso.
    """
    list_display = ('codigo', 'nombre', 'programa', 'semestre', 'creditos', 'activo')
    list_filter = ('programa', 'semestre', 'creditos', 'activo', 'fecha_creacion')
    search_fields = ('nombre', 'codigo', 'descripcion')
    readonly_fields = ('fecha_creacion',)
    list_editable = ('activo',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'codigo', 'programa', 'semestre', 'creditos', 'activo')
        }),
        ('Descripción', {
            'fields': ('descripcion',)
        }),
        ('Información del Sistema', {
            'fields': ('fecha_creacion',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Estudiante.
    """
    list_display = ('numero_identificacion', 'nombres', 'apellidos', 'email', 'programa_principal', 'activo')
    list_filter = ('programa_principal', 'activo', 'fecha_ingreso')
    search_fields = ('numero_identificacion', 'nombres', 'apellidos', 'email')
    date_hierarchy = 'fecha_ingreso'
    list_editable = ('activo',)
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('numero_identificacion', 'nombres', 'apellidos', 'fecha_nacimiento')
        }),
        ('Información de Contacto', {
            'fields': ('email', 'telefono')
        }),
        ('Información Académica', {
            'fields': ('programa_principal', 'fecha_ingreso', 'activo')
        }),
    )


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Inscripción.
    """
    list_display = ('estudiante', 'curso', 'semestre_cursado', 'nota_final', 'aprobado', 'fecha_inscripcion')
    list_filter = ('aprobado', 'semestre_cursado', 'fecha_inscripcion', 'curso__programa')
    search_fields = (
        'estudiante__nombres', 
        'estudiante__apellidos', 
        'estudiante__numero_identificacion',
        'curso__nombre', 
        'curso__codigo'
    )
    date_hierarchy = 'fecha_inscripcion'
    list_editable = ('nota_final', 'aprobado')
    
    fieldsets = (
        ('Información de Inscripción', {
            'fields': ('estudiante', 'curso', 'semestre_cursado')
        }),
        ('Calificaciones', {
            'fields': ('nota_final', 'aprobado')
        }),
        ('Información del Sistema', {
            'fields': ('fecha_inscripcion',),
            'classes': ('collapse',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """Hacer que fecha_inscripcion sea solo lectura"""
        if obj:  # Si es una edición (objeto existente)
            return self.readonly_fields + ('fecha_inscripcion',)
        return self.readonly_fields
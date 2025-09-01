from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q, Count
from .models import Programa, Curso, Estudiante, Inscripcion


# ==================== VISTAS DE PROGRAMAS ====================

class ProgramaListView(ListView):
    """
    Vista que muestra la lista de todos los programas académicos.
    """
    model = Programa
    template_name = 'academico/programas/lista.html'
    context_object_name = 'programas'
    paginate_by = 10

    def get_queryset(self):
        """
        Retorna los programas, con opción de filtrar por búsqueda.
        """
        queryset = Programa.objects.filter(activo=True)
        busqueda = self.request.GET.get('buscar')
        
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) |
                Q(codigo__icontains=busqueda) |
                Q(descripcion__icontains=busqueda)
            )
        
        return queryset.annotate(total_cursos=Count('cursos'))

    def get_context_data(self, **kwargs):
        """Agregar contexto adicional a la template"""
        context = super().get_context_data(**kwargs)
        context['total_programas'] = Programa.objects.filter(activo=True).count()
        context['busqueda'] = self.request.GET.get('buscar', '')
        return context


class ProgramaDetailView(DetailView):
    """
    Vista que muestra el detalle de un programa específico.
    """
    model = Programa
    template_name = 'academico/programas/detalle.html'
    context_object_name = 'programa'

    def get_context_data(self, **kwargs):
        """Agregar información adicional del programa"""
        context = super().get_context_data(**kwargs)
        programa = self.get_object()
        
        # Obtener cursos del programa
        context['cursos'] = programa.cursos.filter(activo=True).order_by('semestre', 'nombre')
        
        # Obtener estudiantes del programa
        context['estudiantes'] = programa.estudiantes.filter(activo=True)[:10]  # Primeros 10
        
        # Estadísticas
        context['total_cursos'] = programa.cursos.filter(activo=True).count()
        context['total_estudiantes'] = programa.estudiantes.filter(activo=True).count()
        
        return context


# ==================== VISTAS DE CURSOS ====================

class CursoListView(ListView):
    """
    Vista que muestra la lista de todos los cursos.
    """
    model = Curso
    template_name = 'academico/cursos/lista.html'
    context_object_name = 'cursos'
    paginate_by = 15

    def get_queryset(self):
        """
        Retorna los cursos con opción de filtrar.
        """
        queryset = Curso.objects.filter(activo=True).select_related('programa')
        busqueda = self.request.GET.get('buscar')
        programa_id = self.request.GET.get('programa')
        
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) |
                Q(codigo__icontains=busqueda) |
                Q(descripcion__icontains=busqueda)
            )
        
        if programa_id:
            queryset = queryset.filter(programa_id=programa_id)
        
        return queryset.annotate(total_estudiantes=Count('inscripciones'))

    def get_context_data(self, **kwargs):
        """Agregar contexto adicional"""
        context = super().get_context_data(**kwargs)
        context['programas'] = Programa.objects.filter(activo=True)
        context['total_cursos'] = Curso.objects.filter(activo=True).count()
        context['busqueda'] = self.request.GET.get('buscar', '')
        context['programa_seleccionado'] = self.request.GET.get('programa', '')
        return context


class CursoDetailView(DetailView):
    """
    Vista que muestra el detalle de un curso específico.
    """
    model = Curso
    template_name = 'academico/cursos/detalle.html'
    context_object_name = 'curso'

    def get_context_data(self, **kwargs):
        """Agregar información adicional del curso"""
        context = super().get_context_data(**kwargs)
        curso = self.get_object()
        
        # Obtener inscripciones del curso
        inscripciones = curso.inscripciones.select_related('estudiante').order_by('-fecha_inscripcion')
        context['inscripciones'] = inscripciones
        
        # Estadísticas
        context['total_inscripciones'] = inscripciones.count()
        context['aprobados'] = inscripciones.filter(aprobado=True).count()
        context['reprobados'] = inscripciones.filter(aprobado=False, nota_final__isnull=False).count()
        
        return context


# ==================== VISTAS DE ESTUDIANTES ====================

class EstudianteListView(ListView):
    """
    Vista que muestra la lista de todos los estudiantes.
    """
    model = Estudiante
    template_name = 'academico/estudiantes/lista.html'
    context_object_name = 'estudiantes'
    paginate_by = 20

    def get_queryset(self):
        """
        Retorna los estudiantes con opción de filtrar.
        """
        queryset = Estudiante.objects.filter(activo=True).select_related('programa_principal')
        busqueda = self.request.GET.get('buscar')
        programa_id = self.request.GET.get('programa')
        
        if busqueda:
            queryset = queryset.filter(
                Q(nombres__icontains=busqueda) |
                Q(apellidos__icontains=busqueda) |
                Q(numero_identificacion__icontains=busqueda) |
                Q(email__icontains=busqueda)
            )
        
        if programa_id:
            queryset = queryset.filter(programa_principal_id=programa_id)
        
        return queryset.annotate(total_cursos=Count('inscripciones'))

    def get_context_data(self, **kwargs):
        """Agregar contexto adicional"""
        context = super().get_context_data(**kwargs)
        context['programas'] = Programa.objects.filter(activo=True)
        context['total_estudiantes'] = Estudiante.objects.filter(activo=True).count()
        context['busqueda'] = self.request.GET.get('buscar', '')
        context['programa_seleccionado'] = self.request.GET.get('programa', '')
        return context


class EstudianteDetailView(DetailView):
    """
    Vista que muestra el detalle de un estudiante específico.
    """
    model = Estudiante
    template_name = 'academico/estudiantes/detalle.html'
    context_object_name = 'estudiante'

    def get_context_data(self, **kwargs):
        """Agregar información académica del estudiante"""
        context = super().get_context_data(**kwargs)
        estudiante = self.get_object()
        
        # Obtener inscripciones del estudiante
        inscripciones = estudiante.inscripciones.select_related('curso', 'curso__programa').order_by('-fecha_inscripcion')
        context['inscripciones'] = inscripciones
        
        # Estadísticas académicas
        context['total_inscripciones'] = inscripciones.count()
        context['cursos_aprobados'] = inscripciones.filter(aprobado=True).count()
        context['cursos_reprobados'] = inscripciones.filter(aprobado=False, nota_final__isnull=False).count()
        
        # Calcular promedio general si hay notas
        notas = inscripciones.filter(nota_final__isnull=False).values_list('nota_final', flat=True)
        if notas:
            context['promedio_general'] = sum(notas) / len(notas)
        else:
            context['promedio_general'] = None
        
        return context


# ==================== VISTAS DE INSCRIPCIONES ====================

class InscripcionListView(ListView):
    """
    Vista que muestra la lista de todas las inscripciones.
    """
    model = Inscripcion
    template_name = 'academico/inscripciones/lista.html'
    context_object_name = 'inscripciones'
    paginate_by = 25

    def get_queryset(self):
        """
        Retorna las inscripciones con opción de filtrar.
        """
        queryset = Inscripcion.objects.select_related(
            'estudiante', 
            'curso', 
            'curso__programa'
        )
        
        busqueda = self.request.GET.get('buscar')
        programa_id = self.request.GET.get('programa')
        semestre = self.request.GET.get('semestre')
        
        if busqueda:
            queryset = queryset.filter(
                Q(estudiante__nombres__icontains=busqueda) |
                Q(estudiante__apellidos__icontains=busqueda) |
                Q(estudiante__numero_identificacion__icontains=busqueda) |
                Q(curso__nombre__icontains=busqueda) |
                Q(curso__codigo__icontains=busqueda)
            )
        
        if programa_id:
            queryset = queryset.filter(curso__programa_id=programa_id)
            
        if semestre:
            queryset = queryset.filter(semestre_cursado=semestre)
        
        return queryset.order_by('-fecha_inscripcion')

    def get_context_data(self, **kwargs):
        """Agregar contexto para filtros"""
        context = super().get_context_data(**kwargs)
        context['programas'] = Programa.objects.filter(activo=True)
        context['semestres'] = Inscripcion.objects.values_list(
            'semestre_cursado', flat=True
        ).distinct().order_by('-semestre_cursado')
        context['total_inscripciones'] = Inscripcion.objects.count()
        context['busqueda'] = self.request.GET.get('buscar', '')
        context['programa_seleccionado'] = self.request.GET.get('programa', '')
        context['semestre_seleccionado'] = self.request.GET.get('semestre', '')
        return context


class InscripcionDetailView(DetailView):
    """
    Vista que muestra el detalle de una inscripción específica.
    """
    model = Inscripcion
    template_name = 'academico/inscripciones/detalle.html'
    context_object_name = 'inscripcion'


# ==================== VISTA DE INICIO ====================

def inicio_view(request):
    """
    Vista de inicio que muestra estadísticas generales del sistema.
    """
    # Recopilar estadísticas generales
    context = {
        'total_programas': Programa.objects.filter(activo=True).count(),
        'total_cursos': Curso.objects.filter(activo=True).count(),
        'total_estudiantes': Estudiante.objects.filter(activo=True).count(),
        'total_inscripciones': Inscripcion.objects.count(),
        
        # Últimos registros
        'programas_recientes': Programa.objects.filter(activo=True).order_by('-fecha_creacion')[:5],
        'estudiantes_recientes': Estudiante.objects.filter(activo=True).order_by('-fecha_ingreso')[:5],
        'inscripciones_recientes': Inscripcion.objects.select_related(
            'estudiante', 'curso'
        ).order_by('-fecha_inscripcion')[:10],
    }
    
    return render(request, 'academico/inicio.html', context)
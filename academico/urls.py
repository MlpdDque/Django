from django.urls import path
from . import views

# Espacio de nombres para las URLs de la aplicación académica
app_name = 'academico'

urlpatterns = [
    # ==================== URLS DE INICIO ====================
    path('', views.inicio_view, name='inicio'),
    
    # ==================== URLS DE PROGRAMAS ====================
    path('programas/', views.ProgramaListView.as_view(), name='programas_lista'),
    path('programas/<int:pk>/', views.ProgramaDetailView.as_view(), name='programa_detalle'),
    
    # ==================== URLS DE CURSOS ====================
    path('cursos/', views.CursoListView.as_view(), name='cursos_lista'),
    path('cursos/<int:pk>/', views.CursoDetailView.as_view(), name='curso_detalle'),
    
    # ==================== URLS DE ESTUDIANTES ====================
    path('estudiantes/', views.EstudianteListView.as_view(), name='estudiantes_lista'),
    path('estudiantes/<int:pk>/', views.EstudianteDetailView.as_view(), name='estudiante_detalle'),
    
    # ==================== URLS DE INSCRIPCIONES ====================
    path('inscripciones/', views.InscripcionListView.as_view(), name='inscripciones_lista'),
    path('inscripciones/<int:pk>/', views.InscripcionDetailView.as_view(), name='inscripcion_detalle'),
]
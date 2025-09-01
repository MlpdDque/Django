from django.apps import AppConfig


class AcademicoConfig(AppConfig):
    """
    Configuración de la aplicación académica.
    Maneja la información de programas, cursos y estudiantes.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'academico'
    verbose_name = 'Sistema Académico'
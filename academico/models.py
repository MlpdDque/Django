from django.db import models
from django.urls import reverse


class Programa(models.Model):
    """
    Modelo que representa un programa académico de la universidad.
    Ejemplo: Ingeniería de Sistemas, Medicina, Derecho, etc.
    """
    nombre = models.CharField(
        max_length=200, 
        verbose_name="Nombre del Programa",
        help_text="Nombre completo del programa académico"
    )
    codigo = models.CharField(
        max_length=10, 
        unique=True,
        verbose_name="Código",
        help_text="Código único identificador del programa"
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción",
        help_text="Descripción detallada del programa"
    )
    duracion_semestres = models.PositiveIntegerField(
        verbose_name="Duración en Semestres",
        help_text="Número de semestres que dura el programa"
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="¿El programa está actualmente activo?"
    )

    class Meta:
        verbose_name = "Programa"
        verbose_name_plural = "Programas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    def get_absolute_url(self):
        """Retorna la URL para ver el detalle de este programa"""
        return reverse('academico:programa_detalle', kwargs={'pk': self.pk})

    def get_total_cursos(self):
        """Retorna el número total de cursos en este programa"""
        return self.cursos.count()


class Curso(models.Model):
    """
    Modelo que representa un curso específico dentro de un programa.
    Ejemplo: Cálculo I, Programación Básica, Anatomía, etc.
    """
    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre del Curso"
    )
    codigo = models.CharField(
        max_length=15,
        unique=True,
        verbose_name="Código del Curso"
    )
    creditos = models.PositiveIntegerField(
        verbose_name="Créditos Académicos",
        help_text="Número de créditos que otorga el curso"
    )
    programa = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name='cursos',
        verbose_name="Programa",
        help_text="Programa al que pertenece este curso"
    )
    semestre = models.PositiveIntegerField(
        verbose_name="Semestre",
        help_text="Semestre en el que se dicta el curso"
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['programa', 'semestre', 'nombre']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    def get_absolute_url(self):
        """Retorna la URL para ver el detalle de este curso"""
        return reverse('academico:curso_detalle', kwargs={'pk': self.pk})

    def get_total_estudiantes(self):
        """Retorna el número total de estudiantes inscritos"""
        return self.inscripciones.count()


class Estudiante(models.Model):
    """
    Modelo que representa un estudiante de la universidad.
    """
    numero_identificacion = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Número de Identificación"
    )
    nombres = models.CharField(
        max_length=100,
        verbose_name="Nombres"
    )
    apellidos = models.CharField(
        max_length=100,
        verbose_name="Apellidos"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Correo Electrónico"
    )
    telefono = models.CharField(
        max_length=15,
        blank=True,
        verbose_name="Teléfono"
    )
    fecha_nacimiento = models.DateField(
        verbose_name="Fecha de Nacimiento"
    )
    programa_principal = models.ForeignKey(
        Programa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='estudiantes',
        verbose_name="Programa Principal",
        help_text="Programa principal en el que está inscrito el estudiante"
    )
    fecha_ingreso = models.DateField(
        verbose_name="Fecha de Ingreso"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f"{self.numero_identificacion} - {self.nombres} {self.apellidos}"

    def get_absolute_url(self):
        """Retorna la URL para ver el detalle de este estudiante"""
        return reverse('academico:estudiante_detalle', kwargs={'pk': self.pk})

    def get_nombre_completo(self):
        """Retorna el nombre completo del estudiante"""
        return f"{self.nombres} {self.apellidos}"

    def get_total_cursos_inscritos(self):
        """Retorna el número total de cursos en los que está inscrito"""
        return self.inscripciones.count()


class Inscripcion(models.Model):
    """
    Modelo que representa la inscripción de un estudiante en un curso específico.
    Esta es la tabla intermedia que conecta estudiantes con cursos.
    """
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='inscripciones',
        verbose_name="Estudiante"
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='inscripciones',
        verbose_name="Curso"
    )
    fecha_inscripcion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Inscripción"
    )
    semestre_cursado = models.CharField(
        max_length=10,
        verbose_name="Semestre Cursado",
        help_text="Ejemplo: 2024-1, 2024-2"
    )
    nota_final = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Nota Final",
        help_text="Nota final del curso (0.0 - 5.0)"
    )
    aprobado = models.BooleanField(
        default=False,
        verbose_name="Aprobado",
        help_text="¿El estudiante aprobó el curso?"
    )

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        # Restricción única: un estudiante no puede inscribirse dos veces al mismo curso
        unique_together = ['estudiante', 'curso']
        ordering = ['-fecha_inscripcion']

    def __str__(self):
        return f"{self.estudiante.get_nombre_completo()} - {self.curso.nombre}"

    def get_absolute_url(self):
        """Retorna la URL para ver el detalle de esta inscripción"""
        return reverse('academico:inscripcion_detalle', kwargs={'pk': self.pk})
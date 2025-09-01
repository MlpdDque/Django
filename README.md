# Sistema Académico Universitario

Una aplicación Django completa para la gestión de información académica básica de una universidad, incluyendo programas, cursos, estudiantes e inscripciones.

## 🎓 Características Principales

- **Gestión de Programas Académicos**: Crear y administrar carreras universitarias
- **Gestión de Cursos**: Organizar cursos por programa y semestre
- **Gestión de Estudiantes**: Registro y seguimiento de estudiantes
- **Sistema de Inscripciones**: Matricular estudiantes en cursos con validaciones
- **Panel de Administración**: Interface completa para administradores
- **Interfaz Web Responsiva**: Vistas públicas con Bootstrap 5

## 🏗️ Estructura del Proyecto

```
universidad/
├── manage.py                      # Comando principal de Django
├── requirements.txt               # Dependencias del proyecto
├── README.md                     # Este archivo
├── universidad/                  # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py              # Configuración de Django
│   ├── urls.py                  # URLs principales
│   ├── wsgi.py                  # Configuración WSGI
│   └── asgi.py                  # Configuración ASGI
├── academico/                   # Aplicación principal
│   ├── __init__.py
│   ├── apps.py                  # Configuración de la app
│   ├── models.py                # Modelos de datos
│   ├── views.py                 # Vistas y lógica
│   ├── urls.py                  # URLs de la aplicación
│   ├── admin.py                 # Configuración del panel admin
│   └── migrations/              # Migraciones de base de datos
└── templates/                   # Plantillas HTML
    ├── base.html               # Template base
    └── academico/              # Templates de la app académica
        ├── inicio.html
        ├── programas/
        ├── cursos/
        ├── estudiantes/
        └── inscripciones/
```

## 📊 Modelos de Datos

### Programa
- Nombre, código único, descripción
- Duración en semestres
- Estado activo/inactivo
- Relación: Un programa tiene muchos cursos

### Curso
- Nombre, código único, descripción
- Número de créditos y semestre
- Pertenece a un programa específico
- Relación: Un curso puede tener muchos estudiantes (a través de inscripciones)

### Estudiante
- Información personal (nombres, apellidos, identificación)
- Información de contacto (email, teléfono)
- Programa principal de estudios
- Relación: Un estudiante puede inscribirse en muchos cursos

### Inscripción
- Conecta estudiantes con cursos
- Información de semestre cursado
- Nota final y estado de aprobación
- Restricción única: Un estudiante no puede inscribirse dos veces al mismo curso

## 🚀 Instrucciones de Instalación

### 1. Prerrequisitos
- Python 3.8+ instalado
- pip (gestor de paquetes de Python)

### 2. Configuración del Entorno

```bash
# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Configuración de la Base de Datos

```bash
# Crear migraciones iniciales
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario para acceder al panel de administración
python manage.py createsuperuser
```

### 4. Ejecutar el Servidor

```bash
# Iniciar servidor de desarrollo
python manage.py runserver

# El sistema estará disponible en: http://127.0.0.1:8000/
# Panel de administración en: http://127.0.0.1:8000/admin/
```

## 📱 Uso del Sistema

### Panel de Administración
1. Accede a `/admin/` con tu cuenta de superusuario
2. Crea programas académicos
3. Agrega cursos a los programas
4. Registra estudiantes
5. Crea inscripciones para matricular estudiantes en cursos

### Interfaz Pública
- **Inicio**: Dashboard con estadísticas generales
- **Programas**: Lista y detalle de programas académicos
- **Cursos**: Lista y detalle de cursos con filtros
- **Estudiantes**: Lista y detalle de estudiantes
- **Inscripciones**: Lista completa de matrículas

## 🔗 URLs Principales

- `/` - Página de inicio
- `/academico/programas/` - Lista de programas
- `/academico/cursos/` - Lista de cursos
- `/academico/estudiantes/` - Lista de estudiantes
- `/academico/inscripciones/` - Lista de inscripciones
- `/admin/` - Panel de administración

## 📤 Subir a GitHub

Para subir este proyecto a GitHub:

1. **Crear repositorio en GitHub**:
   - Ve a https://github.com/new
   - Nombre: `sistema-academico-universitario`
   - Descripción: "Sistema de gestión académica con Django"
   - Selecciona "Public" o "Private" según prefieras

2. **Inicializar Git y subir**:
```bash
# Inicializar repositorio Git
git init

# Agregar archivos
git add .

# Hacer commit inicial
git commit -m "Proyecto inicial: Sistema Académico Universitario con Django"

# Conectar con GitHub (reemplaza con tu usuario y repo)
git remote add origin https://github.com/TU_USUARIO/sistema-academico-universitario.git

# Subir código
git branch -M main
git push -u origin main
```

## 🎯 Reglas de Negocio Implementadas

✅ Un Programa tiene muchos Cursos  
✅ Un Curso pertenece a un Programa  
✅ Un Estudiante puede inscribirse a varios Cursos  
✅ Un Curso puede tener varios Estudiantes  
✅ Una pareja (estudiante, curso) no se repite en Inscripción (unique_together)  
✅ Vistas Lista/Detalle para todas las entidades  

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 4.2+
- **Base de Datos**: SQLite (por defecto, configurable)
- **Frontend**: Bootstrap 5 + Bootstrap Icons
- **Lenguaje**: Python 3.8+

## 📝 Notas de Desarrollo

- Todos los comentarios están en español
- Código organizado y modular
- Validaciones de integridad en los modelos
- Panel de administración completamente configurado
- Interfaz responsive para móviles y escritorio
- Sistema de búsqueda y filtros implementado

## 🤝 Contribuciones

Este proyecto está listo para ser extendido con nuevas funcionalidades como:
- Sistema de notas más complejo
- Horarios de clases
- Profesores y asignaciones
- Reportes académicos
- API REST

---

**Desarrollado con Django** 🚀
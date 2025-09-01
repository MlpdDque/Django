"""
Configuración de URL para el proyecto universidad.

La lista `urlpatterns` enruta las URLs a las vistas. Para más información, consulte:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Ejemplos:
Vistas de función
    1. Agregar una importación:  from my_app import views
    2. Agregar una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clase
    1. Agregar una importación:  from other_app.views import Home
    2. Agregar una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluyendo otra URLconf
    1. Importar la función include(): from django.urls import include, path
    2. Agregar una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Función simple para redirigir la raíz a la app académica
def redirect_to_academico(request):
    return redirect('academico:programas_lista')

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración de Django
    path('', redirect_to_academico),  # Redirigir raíz a la lista de programas
    path('academico/', include('academico.urls')),  # URLs de la aplicación académica
]
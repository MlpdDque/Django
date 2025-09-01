"""
Configuración WSGI para el proyecto universidad.

Expone el callable WSGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulte:
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Establecer el módulo de configuración predeterminado de Django para la aplicación 'universidad'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'universidad.settings')

application = get_wsgi_application()
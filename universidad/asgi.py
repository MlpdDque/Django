"""
Configuración ASGI para el proyecto universidad.

Expone el callable ASGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulte:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Establecer el módulo de configuración predeterminado de Django para la aplicación 'universidad'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'universidad.settings')

application = get_asgi_application()
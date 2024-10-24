import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Llave secreta (en producción, debería estar en las variables de entorno)
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-c7fk++i#)$c(%(7x^_8+o5qmvz_yskx*l%gu#)knfldkd7oru9')

# DEBUG debería estar en False en producción
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# Hosts permitidos (añade Railway u otros dominios de despliegue)
ALLOWED_HOSTS = ['.railway.app', 'localhost', '127.0.0.1']

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'no_lineal',  # Tu aplicación
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de URLs
ROOT_URLCONF = 'proyecto_opti.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'proyecto_opti.wsgi.application'

# Internationalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS, JS, imágenes)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Archivos multimedia (si los usas)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Tipo de campo automático por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración adicional para producción
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Configuración de CSRF (opcional si utilizas dominios específicos)
CSRF_TRUSTED_ORIGINS = ['https://*.railway.app']

# Configuración para servir archivos estáticos desde la plataforma de despliegue
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

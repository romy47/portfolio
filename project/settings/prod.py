from .settings import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['54.163.42.137']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'portfolio',
        'USER': 'himu',
        'PASSWORD': 'unhcevg6.4cec2456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT  = os.path.join(BASE_DIR, 'deployment', 'static')

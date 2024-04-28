from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'portfolio',
        'USER': 'postgres',
        'PASSWORD': 'sebastian123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

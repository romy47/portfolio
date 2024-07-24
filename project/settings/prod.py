from .settings import *
from dotenv import load_dotenv
import socket, os
load_dotenv()
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = os.environ.get('PROD_ALLOWED_HOSTS').split(' ')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PROD_DB_NAME'),
        'USER': os.environ.get('PROD_DB_USER'),
        'PASSWORD': os.environ.get('PROD_DB_PASSWORD'),
        'HOST': os.environ.get('PROD_DB_HOST'),
        'PORT': os.environ.get('PROD_DB_PORT')
    }
}

STATIC_ROOT  = os.path.join(BASE_DIR, 'static')

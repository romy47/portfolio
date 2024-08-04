from .settings import *
from dotenv import load_dotenv
import socket, os
load_dotenv()
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DEV_DB_NAME'),
        'USER': os.environ.get('DEV_DB_USER'),
        'PASSWORD': os.environ.get('DEV_DB_PASSWORD'),
        'HOST': os.environ.get('DEV_DB_HOST'),
        'PORT': os.environ.get('DEV_DB_PORT')
    }
}
SUPERUSER_EMAIL = os.environ.get('DEV_SUPERUSER_EMAIL')
SUPERUSER_USERNAME = os.environ.get('DEV_SUPERUSER_USERNAME')
SUPERUSER_PASSWORD = os.environ.get('DEV_SUPERUSER_PASSWORD')

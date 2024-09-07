import os

from dotenv import load_dotenv

from project.settings import BASE_DIR


load_dotenv()
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = os.environ.get("PROD_ALLOWED_HOST").split(" ")
CSRF_TRUSTED_ORIGINS = ["https://" + host for host in ALLOWED_HOSTS]
CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS + [
    "http://" + host for host in ALLOWED_HOSTS
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("PROD_DB_NAME"),
        "USER": os.environ.get("PROD_DB_USER"),
        "PASSWORD": os.environ.get("PROD_DB_PASSWORD"),
        "HOST": os.environ.get("PROD_DB_HOST"),
        "PORT": os.environ.get("PROD_DB_PORT"),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")

SUPERUSER_EMAIL = os.environ.get("PROD_SUPERUSER_EMAIL")
SUPERUSER_USERNAME = os.environ.get("PROD_SUPERUSER_USERNAME")
SUPERUSER_PASSWORD = os.environ.get("PROD_SUPERUSER_PASSWORD")

#!/bin/sh

python manage.py migrate --noinput
python manage.py create_super_user
python manage.py collectstatic --noinput
gunicorn project.wsgi:application --bind 0.0.0.0:8000

FROM python:3.10-alpine
COPY . /app
WORKDIR /app
EXPOSE 8000
RUN pip install --upgrade pip
RUN apk add postgresql-dev
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic
RUN gunicorn project.wsgi:application --bind 0.0.0.0:8000
FROM python:3.10-alpine
COPY . /app
WORKDIR /app
EXPOSE 8000
RUN pip install --upgrade pip
RUN apk add postgresql-dev
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", ".entrypoint.sh"]
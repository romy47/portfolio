FROM nginx:1.23.0-alpine

COPY ./conf/* /etc/nginx/
COPY setup_nginx_conf.sh /app/
WORKDIR /app
RUN chmod +x setup_nginx_conf.sh
ENTRYPOINT ["sh", "setup_nginx_conf.sh"]
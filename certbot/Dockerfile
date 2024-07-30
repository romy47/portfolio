FROM certbot/certbot:v1.27.0

COPY certbot_init.sh /app/
WORKDIR /app
RUN chmod +x certbot_init.sh
ENTRYPOINT []
CMD ["certbot", "renew"]

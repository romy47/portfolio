FROM certbot/certbot:v1.27.0

COPY certbot-init.sh /app/
RUN chmod +x /app/certbot-init.sh

ENTRYPOINT []
CMD ["certbot", "renew"]

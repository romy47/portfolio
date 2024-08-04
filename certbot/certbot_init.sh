#!/bin/sh

# Waits for nginx to be available, then gets the first certificate.

set -e

# Use netcat (nc) to check port 80, and keep checking every 5 seconds
# until it is available. This is so nginx has time to start before
# certbot runs.
until nc -z nginx 80; do
    echo "Waiting for nginx..."
    sleep 5s & wait ${!}
done

echo "Getting certificate..."

certbot certonly \
    --webroot \
    --webroot-path "/vol/www/" \
    $staging_arg \
    -d "$DOMAIN" \
    --email $EMAIL \
    --rsa-key-size 4096 \
    --agree-tos \
    --noninteractive
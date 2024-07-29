#!/bin/bash

set -e

echo "Checking for dhparams.pem"
if [ ! -f "/vol/nginx_ssl_conf/ssl-dhparams.pem" ]; then
  echo "### Downloading recommended TLS parameters ..."
  mkdir -p "/vol/nginx_ssl_conf/"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > "/vol/nginx_ssl_conf/options-ssl-nginx.conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem > "/vol/nginx_ssl_conf/ssl-dhparams.pem"
  echo
fi

# Avoid replacing these with envsubst
export host=\$host
export request_uri=\$request_uri

echo "Checking for fullchain.pem"
if [ ! -f "/etc/letsencrypt/live/${DOMAIN}/fullchain.pem" ]; then
  echo "No SSL cert, enabling HTTP only..."
  envsubst < /etc/nginx/prod.conf.pre-ssl.template > /etc/nginx/conf.d/default.conf
else
  echo "SSL cert exists, enabling HTTPS..."
  envsubst < /etc/nginx/prod.conf.ssl.template > /etc/nginx/conf.d/default.conf
fi

nginx -g 'daemon off;'




















#!/bin/bash

# Source the .env file
if [ -f .env ]; then
  export $(cat .env | grep -v '#' | awk '/=/ {print $1}')
fi
# Check the value of the environment variable and copy the corresponding file
if [ "$IS_DEV" = "True" ]; then
    echo "dev.conf"
    cp /dev.conf /etc/nginx/conf.d/default.conf
elif [ "$IS_DEV" = "False" ]; then
    echo "prod.conf"
    cp /prod.conf.template /etc/nginx/conf.d/default.conf.template
    # Substitute the environment variables in the template and create the actual nginx.conf
    envsubst < /etc/nginx/conf.d/default.conf > /etc/nginx/conf.d/default.conf.template
else
    echo "No valid file specified to copy"
    exit 1
fi
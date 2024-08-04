#!/bin/sh

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
export http_host=\$http_host
export remote_addr=\$remote_addr
export proxy_add_x_forwarded_for=\$proxy_add_x_forwarded_for
export scheme=\$scheme;

echo "Checking for fullchain.pem"
if [ ! -f "/etc/letsencrypt/live/${DOMAIN}/fullchain.pem" ]; then
  echo "No SSL cert, enabling HTTP only..."
  envsubst < /etc/nginx/prod.conf.pre-ssl.template > /etc/nginx/conf.d/default.conf
else
  echo "SSL cert exists, enabling HTTPS..."
  envsubst < /etc/nginx/prod.conf.ssl.template > /etc/nginx/conf.d/default.conf
fi

nginx -g 'daemon off;'

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
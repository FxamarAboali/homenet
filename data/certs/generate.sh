#!/usr/bin/env bash

DOMAIN="$1"

if [[ ! "$DOMAIN" ]]; then
    echo "Generate a self-signed SSL certificate and Diffie-helman parameters for a given [domain]"
    echo ""
    echo "Usage:"
    echo "    ./generate.sh [domain]"
    echo ""
    echo "Examples:"
    echo "    ./generate.sh homenet.l"
    echo "    ./generate.sh homenet.zalad.io"
    echo "    ./generate.sh homenet.com"
    exit 2
fi

openssl dhparam -out "$DOMAIN.dh" 2048

# You can either:
#
# 1. generate a self-signed cert with openssl
#
#openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out "$DOMAIN.crt" -keyout "$DOMAIN.key" -subj "/C=US/ST=NY/L=New York/O=Monadical/OU=Engineering/CN=$DOMAIN"
#
# 2. Or use mkcert to install a trusted local dev cert (https://github.com/FiloSottile/mkcert)

if brew --version > /dev/null; then
    brew install mkcert
else
    apt install -y mkcert
fi

mkcert "$DOMAIN"
mv "$DOMAIN.pem" "$DOMAIN.crt"
mv "$DOMAIN-key.pem" "$DOMAIN.key"
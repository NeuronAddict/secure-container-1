#! /usr/bin/env bash

openssl req -new -newkey rsa:2048 \
        -keyout secure-container.local.key \
        -out secure-container.local.csr \
        -subj "/C=FR/ST=France/L=Paris/O=Wood and Safety/OU=neuronaddict/CN=secure-container.local"

openssl x509 -req -days 365 -in secure-container.local.csr -signkey secure-container.local.key -out secure-container.local.crt

chmod g+r secure-container.local.key
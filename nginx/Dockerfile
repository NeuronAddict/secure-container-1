FROM docker.io/bitnami/nginx:latest

ARG SSL_PASSWORD

RUN echo ${SSL_PASSWORD} > /opt/bitnami/nginx/ssl-nginx.pass

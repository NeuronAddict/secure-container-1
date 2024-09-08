FROM docker.io/library/nginx:1.27

ARG SSL_PASSWORD

RUN echo ${SSL_PASSWORD} > /etc/nginx/ssl-nginx.pass

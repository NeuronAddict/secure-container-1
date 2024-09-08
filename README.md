# secure container demo

## How to

```
$ cd gradio-backend/models
$ git clone https://huggingface.co/CATIE-AQ/QAmembert # https://huggingface.co/CATIE-AQ/QAmembert?clone=true
$ cd -
$ cd nginx
$ bash mkcert.sh
$ # choisir un mot de passe et le mettre dans le docker compose
$ cd -
$ cp .env.example .env # custom if needed
$ docker compose up --build # or docker-compose up --build
```

L'application est disponible sur le port 8443 en https.

## Certificat 

Solution facile : Accepter le certificat quand le navigateur le demande
Solution propre : Ajouter le certificat dans firefox. Conseil : le faire sur une session à part.

#! /usr/bin/bash

clear

for message in "Je n'expose pas mes conteneurs en root" "jamais" "Je n'en ai pas besoin" "Merci aux développeurs de docker, de linux, etc." "Merci à tous" "A bientôt"
do
  toilet -w 146 -k -f big "$message" | lolcat -a -d 7 -s 20
done

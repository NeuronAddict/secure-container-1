#! /usr/bin/bash

clear

for message in "Une bonne image de base" "Une exposition prudente des ports" "Des secrets bien gardés" "Merci aux développeurs de docker" "Merci à OVH pour son serveur"  "Merci à tous" "A bientôt"
do
  toilet -w 146 -k -f big "$message" | lolcat -a -d 7 -s 20
done

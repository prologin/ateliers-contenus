# Prolobot

<!-- TODO: Introduction -->

## Utiliser avec Mu-editor

- Déplacer le fichier `prolobot.py` dans le dossier source de mu-editor
- Appuyer sur le bouton fichier
- Glisser le fichier de `Sur mon ordinateur` a `Sur le microbit`
- Flasher le microbit
- Brancher le microbit au robot et l'allumer

## La Doc

<!-- NOTE: La doc est temporaire, si elle reste ca sera juste a la fin pour
    en tant que recap -->

### Instantier le robot

```py
import prolobot

bot = Prolobot()
```

### Variables globales

`GAUCHE = 0`. A donner en parametre pour tourner a gauche.
`DROITE = 1`. A donner en parametre pour tourner a droite.

### Fonctions

#### Deplacement

`bot.avancer()`: avance le robot.
- La vitesse par defaut est 0.2

`bot.avancer(vitesse)`: avance a la vitesse donnee.
- La vitesse est un float entre 0 et 1.

`bot.reculer()`: recule le robot.
- La vitesse par defaut est 0.2.

`bot.reculer(vitesse)`: recule le robot a la vitesse donnee.
- La vitesse est un float entre 0 et 1.

`bot.tourner(direction)`: tourne le robot dans la direction donnee. 
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction.

`bot.tourner(direction, vitesse)`: tourne le robot dans la direction et a la vitesse donnee.
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction
- La vitesse est entre 0 et 1

`bot.pivoter(direction)`: tourne le robot sur lui même dans la direction donnee. 
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction.

`bot.pivoter(direction, vitesse)`: tourne le robot sur lui même dans la direction et a la vitesse donnee.
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer la direction
- La vitesse est entre 0 et 1

`bot.stop()`: arrete le robot.

#### Capteurs

`bot.distance()`: renvoie la distance entre le robot et les obstacles en face de lui.

`bot.capteur_sol(capteur)`: renvoie 1 si le capteur detecte du noir.
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer quel capteur utiliser.

#### LEDs

`bot.allumer_phares(phare, statut)`: allume ou eteint un des phares avant,
- On peut utiliser les constantes `DROITE` et `GAUCHE` pour indiquer quel capteur utiliser.
- Le statut est a 1 pour allumer et 0 pour eteindre la led

`bot.allumer_led(led, couleur)`: allume la led correspondante.
- La led est un entier de 0 a 3 servant a preciser la led a allumer
- La couleur est de la forme (rouge, vert, bleu), avec les couleurs allant de 0 a 255

`bot.eteindre_led()`: eteint toutes les leds

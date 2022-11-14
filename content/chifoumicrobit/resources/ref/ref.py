from microbit import *
from random import randint

# La liste des possibilités
possibilites = [Image.SKULL, Image.PACMAN, Image.GHOST]

# Le nombre de possibilités
# La fonction `len` renvoie la longueur d'une liste
NB_POSSIBILITES = len(possibilites)

# Choix aléatoire du micro:bit
# entre 0 et `NB_POSSIBILITES` exclu
choix_adversaire = randint(0, NB_POSSIBILITES - 1)

# Le choix du joueur est à 0 par défaut
choix_joueur = 0

# On affiche le choix actuel le temps qu'il n'est pas validé
# par un appui simultané sur A et B
while not (button_a.is_pressed() and button_b.is_pressed()):
    # Affiche le choix actuel du joueur
    display.show(possibilites[choix_joueur])

    # Si A est appuyé
    if button_a.was_pressed():
        # On enlève 1 au choix du joueur
        # Le modulo permet de revenir au début de la liste des choix
        choix_joueur = (choix_joueur - 1) % NB_POSSIBILITES

    # Si B est appuyé
    if button_b.was_pressed():
        # On ajoute 1 au choix du joueur
        # Le modulo permet de revenir au début de la liste des choix
        choix_joueur = (choix_joueur + 1) % NB_POSSIBILITES

    # Permet de mettre en pause le programme
    # le temps de lire l'entrée du joueur
    sleep(100)

# Éteint toutes les LEDs de l'écran
display.clear()
sleep(500)

# Affiche le choix du joueur
display.show(possibilites[choix_joueur])
sleep(2000)

display.scroll("VS")

# Affiche le choix du micro:bit
display.show(possibilites[choix_adversaire])
sleep(2000)

# Égalité si les joueurs ont fait le même choix
if choix_joueur == choix_adversaire:
    display.scroll("Egalite !", delay=50)

# Tu as gagné si notre choix bat celui de l'adversaire
elif choix_joueur == 0 and choix_adversaire == 1:
    display.scroll("Gagne !", delay=50)

elif choix_joueur == 1 and choix_adversaire == 2:
    display.scroll("Gagne !", delay=50)

elif choix_joueur == 2 and choix_adversaire == 0:
    display.scroll("Gagne !", delay=50)

# Tu as perdu sinon
else:
    display.scroll("Perdu...", delay=50)

from microbit import *
from random import randint

def genere_mur():
   """
    renvoie 2 entiers correspondant aux positions du nouveau mur généré,
    voir le schéma sur le sujet.
   """
   pass

def affiche_mur(mur_x, intensite, mur_y1, mur_y2):
    """
    @mur_x : colonne où est situé le mur à afficher
    @intensite : intensité des leds du mur
    
    affiche le mur sur le microbit
    """
    pass

def efface_mur(mur_x):
    """
    @mur_x : colonne du mur

    met l'intensité de la colonne à 0.
    """
    pass

def deplace_mur(mur_x, intensite ,mur_y1, mur_y2):
    """
    @mur_x ; ancienne colonne du mur
    @intensité : intensité des leds du mur

    déplace le mur d'un cran vers la gauche
    valeur retournée : nouvelle colonne du mur
    """
    pass

def affiche_joueur(joueur_x, joueur_y, intensite):
    """
    @joueur_x, joueur_y : coordonnées du joueur
    @instensite : intensité des leds du mur

    affiche le joueur sur l'ecran
    """
    pass

def collision(joueur_x, joueur_y, mur_x, mur_y1, mur_y2):
    """
    @joueur_x, joueur_y : coordonnées du joueur
    @mur_x : colonne actuelle du mur
    @mur_y1, mur_y2 : hauteur du mur
    
    vérifie si le joueur est en collision avec un mur
    valeur retournee : True False 
    """
    pass

def deplace_joueur(joueur_x, joueur_y, joueur_intensite):
    """
    @joueur_x, joueur_y : coordonnées du joueur
    @joueur_intensité : intensité de la led représentant du joueur
    
    vérifie si le joueur a appuyé sur un bouton, et le déplace dans la direction voulue
    """
    pass

# variables initiales du joueur
joueur_x = 1
joueur_y = 2
joueur_intensite = 2

# variables initiales du mur
mur_intensite = 9
mur_x = 5
mur_y1, mur_y2 = genere_mur()

# variables initiales du jeu
en_cours = True
temps = 1000
score = 0
reduction_temps = 50
min_temps = 100

while en_cours:
    # déplace de un vers la gauche (déplacement négatif)
    
    # déplace le joueur en fonction des boutons appuyé
    # bouton_a peut faire monter de 1 case
    # bouton_b peut faire descendre de 1 case

    if """ regarde la collision entre le joueur et le mur """:
        # met en_cours à faux
        # efface le mur
        pass

    if """verifie si le mur est derrière le joueur""":
        # efface le mur
        # génere un nouveau mur et le place à droite de l'écran
        # augmente le score de 1

        # gestion du temps, ne pas toucher
        temps = temps - reduction_temps
        if temps < min_temps:
            temps = min_temps
    
    # arrete le program pendant 'temps' millisecondes
    sleep(temps)

# affiche "Game Over ! Score : " + le score
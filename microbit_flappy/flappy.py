from microbit import *
from random import randint

def genere_tuyaux():
   """
    renvoie 2 entiers correspondant aux positions du nouveau tuyaux généré,
    voir le schéma sur le sujet.
   """
   pass

def affiche_tuyaux(tuyau_x, intensite, tuyau_y1, tuyau_y2):
    """
    @tuyau_x : colonne où est situé le tuyaux à afficher
    @intensite : intensité des leds du tuyaux
    
    affiche le tuyaux sur le microbit
    """
    pass

def efface_tuyaux(tuyau_x):
    """
    @tuyau_x : colonne du tuyaux

    met l'intensité des pixels de la colonne à 0.
    """
    pass

def deplace_tuyaux(tuyau_x, intensite ,tuyau_y1, tuyau_y2):
    """
    @tuyau_x ; ancienne colonne du tuyaux
    @intensité : intensité des leds du tuyaux

    déplace le tuyaux d'un cran vers la gauche
    valeur retournée : nouvelle colonne du tuyaux
    """
    pass

def affiche_oiseau(oiseau_x, oiseau_y, intensite):
    """
    @oiseau_x, oiseau_y : coordonnées du oiseau
    @instensite : intensité des leds du tuyaux

    affiche le oiseau sur l'ecran
    """
    pass

def collision(oiseau_x, oiseau_y, tuyau_x, tuyau_y1, tuyau_y2):
    """
    @oiseau_x, oiseau_y : coordonnées du oiseau
    @tuyau_x : colonne actuelle du tuyaux
    @tuyau_y1, tuyau_y2 : hauteur du tuyaux
    
    vérifie si le oiseau est en collision avec un tuyaux
    valeur retournée : True False 
    """
    pass

def deplace_oiseau(oiseau_x, oiseau_y, oiseau_intensite):
    """
    @oiseau_x, oiseau_y : coordonnées du oiseau
    @oiseau_intensité : intensité de la led représentant du oiseau
    
    vérifie si le oiseau a appuyé sur un bouton, et le déplace dans la direction voulue
    """
    pass

# variables initiales du oiseau
oiseau_x = 1
oiseau_y = 2
oiseau_intensite = 2

# variables initiales du tuyaux
tuyaux_intensite = 9
tuyau_x = 5
tuyau_y1, tuyau_y2 = genere_tuyaux()

# variables initiales du jeu
en_cours = True
temps = 1000
score = 0
reduction_temps = 50
min_temps = 100

while en_cours:
    # déplace de un vers la gauche (déplacement négatif)
    
    # déplace l'oiseau en fonction des boutons appuyé
    # bouton_a peut faire monter de 1 case
    # bouton_b peut faire descendre de 1 case

    if """ regarde la collision entre le oiseau et le tuyaux """:
        # met en_cours à faux
        # efface le tuyaux
        pass

    if """verifie si le tuyaux est derrière le oiseau""":
        # efface le tuyaux
        # génere un nouveau tuyaux et le place à droite de l'écran
        # augmente le score de 1

        # gestion du temps, ne pas toucher
        temps = temps - reduction_temps
        if temps < min_temps:
            temps = min_temps
    
    # arrete le program pendant 'temps' millisecondes
    sleep(temps)

# affiche "Game Over ! Score : " + le score
from microbit import *
from random import randint

def genere_mur():
    mur_y1 = randint(0, 2)
    mur_y2 = randint(mur_y1 + 2, 4)
    return mur_y1, mur_y2

def affiche_mur(x, intensite, mur_y1, mur_y2):
    for i in range(mur_y1 + 1):
        display.set_pixel(x, i, intensite)
    for i in range(mur_y2, 5):
        display.set_pixel(x, i, intensite)

def efface_mur(mur_x):
    for i in range(5):
        display.set_pixel(mur_x, i, 0)

def deplace_mur(mur_x, intensite ,mur_y1, mur_y2):
    if mur_x < 5:
        efface_mur(mur_x)
    affiche_mur(mur_x - 1, intensite, mur_y1, mur_y2)
    return mur_x - 1

def affiche_joueur(joueur_x, joueur_y, intensite):
    display.set_pixel(joueur_x, joueur_y, intensite)

def collision(joueur_x, joueur_y, mur_x, mur_y1, mur_y2):
    return joueur_x == mur_x and not (mur_y1 < joueur_y < mur_y2)

def deplace_joueur(joueur_x, joueur_y, joueur_intensite):
    affiche_joueur(joueur_x, joueur_y, 0)
    haut = button_a.get_presses()
    bas = button_b.get_presses()
    joueur_y = joueur_y - haut
    joueur_y = joueur_y + bas
    if joueur_y < 0:
        joueur_y = 0

    if joueur_y > 4:
        joueur_y = 4

    affiche_joueur(joueur_x, joueur_y, joueur_intensite)

    return joueur_y

joueur_x = 1
joueur_y = 2
joueur_intensite = 2

mur_intensite = 9
mur_x = 5
mur_y1, mur_y2 = genere_mur()


en_cours = True
temps = 1000
score = 0
reduction_temps = 50
min_temps = 100

while en_cours:
    mur_x = deplace_mur(mur_x, mur_intensite, mur_y1, mur_y2)
    joueur_y = deplace_joueur(joueur_x, joueur_y, joueur_intensite)
    if collision(joueur_x, joueur_y, mur_x, mur_y1, mur_y2):
        en_cours = False
        affiche_mur(mur_x, 0, mur_y1, mur_y2)
    if mur_x < joueur_x:
        score = score + 1
        mur_y1, mur_y2 = genere_mur()
        efface_mur(mur_x)
        temps = temps - reduction_temps
        if temps < min_temps:
            temps = min_temps
        mur_x = 5

    sleep(temps)


display.scroll("Game Over! Score: " + str(score))

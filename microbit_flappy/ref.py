from microbit import *
from random import randint


def genere_tuyaux():
    tuyau_y1 = randint(0, 2)
    tuyau_y2 = randint(tuyau_y1 + 2, 4)
    return tuyau_y1, tuyau_y2


def affiche_tuyaux(x, intensite, tuyau_y1, tuyau_y2):
    for i in range(tuyau_y1 + 1):
        display.set_pixel(x, i, intensite)
    for i in range(tuyau_y2, 5):
        display.set_pixel(x, i, intensite)


def efface_tuyaux(tuyau_x):
    for i in range(5):
        display.set_pixel(tuyau_x, i, 0)


def deplace_tuyaux(tuyau_x, intensite, tuyau_y1, tuyau_y2):
    if tuyau_x < 5:
        efface_tuyaux(tuyau_x)
    affiche_tuyaux(tuyau_x - 1, intensite, tuyau_y1, tuyau_y2)
    return tuyau_x - 1


def affiche_oiseau(oiseau_x, oiseau_y, intensite):
    display.set_pixel(oiseau_x, oiseau_y, intensite)


def collision(oiseau_x, oiseau_y, tuyau_x, tuyau_y1, tuyau_y2):
    return oiseau_x == tuyau_x and not (tuyau_y1 < oiseau_y < tuyau_y2)


def deplace_oiseau(oiseau_x, oiseau_y, oiseau_intensite):
    affiche_oiseau(oiseau_x, oiseau_y, 0)
    haut = button_a.get_presses()
    bas = button_b.get_presses()
    oiseau_y = oiseau_y - haut
    oiseau_y = oiseau_y + bas
    if oiseau_y < 0:
        oiseau_y = 0

    if oiseau_y > 4:
        oiseau_y = 4

    affiche_oiseau(oiseau_x, oiseau_y, oiseau_intensite)

    return oiseau_y


oiseau_x = 1
oiseau_y = 2
oiseau_intensite = 2

tuyaux_intensite = 9
tuyau_x = 5
tuyau_y1, tuyau_y2 = genere_tuyaux()

temps = 1000
score = 0
reduction_temps = 50
min_temps = 100


while True:
    tuyau_x = deplace_tuyaux(tuyau_x, tuyaux_intensite, tuyau_y1, tuyau_y2)
    oiseau_y = deplace_oiseau(oiseau_x, oiseau_y, oiseau_intensite)
    if collision(oiseau_x, oiseau_y, tuyau_x, tuyau_y1, tuyau_y2):
        break
    if tuyau_x < oiseau_x:
        score = score + 1
        tuyau_y1, tuyau_y2 = genere_tuyaux()
        efface_tuyaux(tuyau_x)

        temps = temps - reduction_temps
        if temps < min_temps:
            temps = min_temps
        tuyau_x = 5

    sleep(temps)


display.scroll("Game Over! Score: " + str(score))

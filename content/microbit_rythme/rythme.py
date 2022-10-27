# import des bibliothèques
from microbit import *
import random as rd

# La boucle principale
notes = [0] # Les notes sur la voie A
while True:

    display.clear()
    ### Affichage ###
    for n in notes: 
        display.set_pixel(4-n%5,0,9)
    
    # Il y a un clap quand une note arrive à la dernière case
    clap = 4 in notes

    # Les notes avancent de 1
    notes = [n+1 for n in notes if n+1 <5 ]
    
    # Ajout d'une nouvelle note
    # TODO 


    # Petite pause
    sleep(1000)
    
    # On teste si l'appuie de bouton correspond à la présence de notes
    if button_a.was_pressed() == clap:
        pass
    else:
        display.show("perdu")
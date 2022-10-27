# import des bibliothèques
from microbit import *
import music
import random as rd



# La boucle principale
while True:
    notesA = [0] # Les notes sur la voie A
    notesB = [] # Les notes sur la voie B
    speed = 1000
    score = 0
    vies = 3
    while vies >0: # La boucle de jeu
        display.clear()
        ### Affichage ###
        for n in notesA: 
            display.set_pixel(4-n%5,0,9)
            display.set_pixel(4-n%5,1,9)
        
        for n in notesB:
            display.set_pixel(n%5,4,9)
            display.set_pixel(n%5,3,9)
        
        for i in range(vies):
            display.set_pixel(i+1,2,9)
        
        # Il y a un clap quand une note arrive à la fin de la ligne 
        clapA = 4 in notesA
        clapB = 4 in notesB

        # Les notes avancent de 1
        notesA = [n+1 for n in notesA if n+1 <5 ]
        notesB = [n+1 for n in notesB if n+1 <5 ]

        # Ajout d'une nouvelle note
        if rd.random() < 1./2 :
            if rd.random() < 1./2 :
                notesA += [0]
            else:
                notesB += [0]

        # Acceleration du petite pause et accélération
        sleep(speed)
        speed *= 0.995
        
        # On teste si l'appuie de bouton correspond à la présence de notes
        if button_a.was_pressed() == clapA and button_b.was_pressed() == clapB:
            score += 1
        else:
            vies -=1
            notesA = []
            notesB = []

    display.scroll("PERDU")
    display.scroll(score)
        

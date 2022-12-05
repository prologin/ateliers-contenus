# import des bibliothèques
from microbit import *
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
            display.set_pixel(4-n,0,9)
            display.set_pixel(4-n,1,9)
        
        for n in notesB:
            display.set_pixel(n,4,9)
            display.set_pixel(n,3,9)
        
        for i in range(vies):
            display.set_pixel(i+1,2,9)
        
        # Il y a un clap quand une note arrive à la fin de la ligne 
        clapA = False
        for note in notesA:
            if note == 4:
                clapA = True
        
        clapB = False
        for note in notesB:
            if note == 4:
                clapB = True
        

        # Les notes avancent de 1
        nouvellesNotesA = []
        for note in notesA:
            if note+1 < 5:
                nouvellesNotesA.append(note+1)
        nouvellesNotesB = []
        for note in notesB:
            if note+1 < 5:
                nouvellesNotesB.append(note+1)
        notesA = nouvellesNotesA
        notesB = nouvellesNotesB

        # Ajout d'une nouvelle note
        if rd.random() < 1./2 :
            if rd.random() < 1./2 :
                notesA.append(0)
            else:
                notesB.append(0)

        # Acceleration du petite pause et accélération
        sleep(speed)
        speed *= 0.995
        
        # On teste si l'appuie de bouton correspond à la présence de notes
        if button_a.was_pressed() == clapA and button_b.was_pressed() == clapB:
            score = score + 1
        else:
            vies = vies - 1
            notesA = []
            notesB = []

    display.scroll("PERDU")
    display.scroll(score)
        

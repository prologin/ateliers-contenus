import pygame

def message_render(message,police,couleur):
    message = police.render(message,True,pygame.Color(couleur))
    return message

def police_taille(taille):
    return pygame.font.Font("BradBunR.ttf",taille)

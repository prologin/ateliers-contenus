import pygame

def message_render(message,police,coul):
    mess = police.render(message,True,pygame.Color(coul))
    return mess

def make_font(font,size):
    return pygame.font.Font(font,size)

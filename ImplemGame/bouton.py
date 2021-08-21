from utils import message_render,  police_taille
import pygame

class Bouton ():
    
    def __init__ (self, x, y, texte, taille, couleur1, couleur2, fonction, ecran):
        self.ecran = ecran
        self.texte = texte
        self.taille = taille
        self.message = message_render(texte, police_taille(self.taille),couleur1)
        self.largeur = self.message.get_width()
        self.hauteur = self.message.get_height()

        self.coords = (x-(self.largeur//2),y-(self.hauteur//2))
        self.rect = pygame.Rect(self.coords[0], self.coords[1], self.largeur, self.hauteur)
        self.couleurs = [couleur1,couleur2]
        self.fonction = fonction

    def change_couleur (self, state):
        self.message = message_render(self.texte, police_taille(self.taille),
                                   self.couleurs[1] if state else self.couleurs[0])


    def clique (self):
        return self.fonction()

    def dessine (self):
        self.ecran.blit (self.message,self.coords)






        

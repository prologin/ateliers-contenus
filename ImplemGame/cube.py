import pygame


class Cube ():

    def __init__ (self, x, y, largeur, hauteur, ecran):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,largeur,hauteur)
        self.mini_rect = pygame.Rect(x+(largeur//10),y+(hauteur//10),largeur-(largeur//5),hauteur-(hauteur//5))
        self.ecran = ecran
        self.couleur = pygame.Color("black")
        self.mini_couleur = pygame.Color("grey39")

    def dessine (self):
        pygame.draw.rect (self.ecran, self.couleur,self.rect)
        pygame.draw.rect (self.ecran, self.mini_couleur,self.mini_rect)

class Piece ():
    def __init__ (self, x, y, largeur, hauteur, ecran):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,largeur,hauteur)
        self.ecran = ecran
        self.couleur = pygame.Color("yellow")
        
    def dessine (self):
        pygame.draw.rect (self.ecran, self.couleur,self.rect)

class Victoire ():
    def __init__ (self, x, y, largeur, hauteur, ecran):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,largeur,hauteur)
        self.ecran = ecran
        self.couleur = pygame.Color("green")

    def dessine (self):
        pygame.draw.rect (self.ecran, self.couleur,self.rect)

class Porte ():
    def __init__ (self, x, y, largeur, hauteur, ecran):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,largeur,hauteur)
        self.ecran = ecran
        self.couleur = pygame.Color("brown")

    def dessine (self):
        pygame.draw.rect (self.ecran, self.couleur,self.rect)

class Clef ():

    def __init__ (self, x, y, largeur, hauteur, ecran):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,largeur,hauteur)
        self.mini_rect = pygame.Rect(x+(largeur//10),y+(hauteur//10),largeur-(largeur//5),hauteur-(hauteur//5))
        self.ecran = ecran
        self.couleur = pygame.Color("black")
        self.mini_couleur = pygame.Color("yellow")

    def dessine (self):
        pygame.draw.rect (self.ecran, self.couleur,self.rect)
        pygame.draw.rect (self.ecran, self.mini_couleur,self.mini_rect)


class Cassable ():

    def __init__ (self, x, y, largeur, hauteur, ecran):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,largeur,hauteur)
        self.mini_rect = pygame.Rect(x+(largeur//10),y+(hauteur//10),largeur-(largeur//5),hauteur-(hauteur//5))
        self.ecran = ecran
        self.couleur = pygame.Color("black")
        self.mini_couleur = pygame.Color("brown")

    def dessine (self):
        pygame.draw.rect (self.ecran, self.couleur,self.rect)
        pygame.draw.rect (self.ecran, self.mini_couleur,self.mini_rect)

import pygame
from pygame.locals import*
from bouton import Bouton




class MenuProchainNiveau ():

    def __init__ (self, largeur, hauteur, ecran):
        self.ecran = ecran
        self.largeur = largeur
        self.hauteur = hauteur
        self.timeur = pygame.time.Clock()
        self.ips = 60
        self.running = True
        self.boutons = [Bouton(self.largeur//2,self.hauteur//4,"Prochain niveau!",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda :  2,
                               self.ecran),
                        Bouton(self.largeur//2,2*self.hauteur//4,"Options!",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda : 1,
                               self.ecran),
                        Bouton(self.largeur//2,3*self.hauteur//4,"Quitter!",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda : 0,
                               self.ecran),
        ]
            
            
    def affichage (self):
        """
        Redessine l'écran de jeu pour chaque image par second
        """

        self.ecran.fill(pygame.Color("gray"))
        for b in self.boutons:
            b.dessine()

        pygame.display.update()
        self.timeur.tick(self.ips)
       


    def update (self):
        pass

    def gestion_evenement (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == MOUSEBUTTONDOWN:
                
                for b in self.boutons:
                    if pygame.Rect.collidepoint(b.rect,event.pos):
                        return b.clique()
                        
                    
            if event.type == MOUSEMOTION:
                for b in self.boutons:
                    b.change_couleur(pygame.Rect.collidepoint(b.rect,event.pos))
               

        
        

    def run (self):
        while self.running:

            res_events = self.gestion_evenement()
            if res_events != None:
                return res_events
            self.update()
            self.affichage()
            

    def __str__(self):
        return "It's a menu bro !"





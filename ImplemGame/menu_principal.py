import pygame
from pygame.locals import*
from bouton import Bouton





class MenuPrincipal ():
    """
    Cette class sert à implémenter le menu principal du jeu
    
    """

    def __init__ (self, largeur, hauteur, ecran):
        self.ecran = ecran
        self.largeur = largeur
        self.hauteur = hauteur
        self.timeur = pygame.time.Clock()
        self.ips = 60
        self.running = True
        self.boutons = [Bouton(self.largeur//2,self.hauteur//4,"Jouer!",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda : 2,
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
            
            
    def affiche (self):
        """
        Raffrachie l'affichage du meny principale
        """

        # rempli le fond de l'écran par du gris
        self.ecran.fill(pygame.Color("gray"))

        # pour tous les boutons, les dessiner
        for b in self.boutons:
            b.dessine()

        # on update l'écran de jeu et on limite le raffraichissement à self.ips images/second
        pygame.display.update()
        self.timeur.tick(self.ips)
       


    def update (self):
        pass

    def gestion_evenement (self):
        """
        Gère les événements pendant le jeu
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            # détection d'un clique sur un bouton
            if event.type == MOUSEBUTTONDOWN:
                for b in self.boutons:
                    if pygame.Rect.collidepoint(b.rect,event.pos):
                        return b.clique()

            # détection du survole d'un bouton
            if event.type == MOUSEMOTION:
                for b in self.boutons:
                    b.change_couleur (pygame.Rect.collidepoint(b.rect, event.pos))
               

        
        

    def run (self):
        """
        Boucle du menu principal
        """
        while self.running:

            # récupère la valeur de retour des événements
            res_events = self.gestion_evenement()

            # si elle n'est pas None cela veut dire qu'un bouton a été cliqué
            if res_events != None:
                return res_events

            self.update()
            self.affiche()
            
        
    def __str__(self):
        return "Menu Principal"

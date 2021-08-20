import pygame
from pygame.locals import*
from bouton import Bouton
from utils import make_font, message_render
from chargeur_niveau import chargeur_niveau



class Jeu ():

    def __init__ (self, largeur, hauteur, ecran, niveau):
        self.ecran = ecran
        self.largeur = largeur
        self.hauteur = hauteur
        self.timeur = pygame.time.Clock()
        self.ips = 60
        self.running = True
        self.options_active = False
        self.indice_active = False
        self.boutons = [Bouton(24*self.largeur//25,self.hauteur//15,"II",100,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda : 1,
                               self.ecran),
                        Bouton(self.largeur//25,self.hauteur//15,"H",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda  : 0,
                               self.ecran),
        ]
        self.boutons_option = [Bouton(21*self.largeur//25,self.hauteur//15,"R",100,
                                     pygame.Color("white"),
                                     pygame.Color("red"),
                                     lambda  : 2,
                                     self.ecran),
                              Bouton(17*self.largeur//25,self.hauteur//15,"Q",100,
                                     pygame.Color("white"),
                                     pygame.Color("red"),
                                     lambda  : 1,
                                     self.ecran),
                              Bouton(13*self.largeur//25,self.hauteur//15,"S",100,
                                     pygame.Color("white"),
                                     pygame.Color("red"),
                                     lambda  : 0,
                                     self.ecran),
        ]
        self.niveau, self.joueur = chargeur_niveau(f"levels/{niveau}.txt", 40, self.ecran)
        if self.joueur == None:
            raise ValueError("Le fichier du niveau ne contient pas de jouer")
        self.joueur.niveau = self.niveau
        
        self.indice_txt = f"Tu dois modifier dans le fichier joueur.py la fonction mouv"
        self.indice = message_render(self.indice_txt,make_font("BradBunR.ttf", 20),pygame.Color("black"))
            
            
    def affiche (self):
        self.ecran.fill(pygame.Color("gray"))
      
        self.niveau.dessine()

        self.joueur.dessine()

        for b in self.boutons:
            b.dessine()
            
        if self.options_active:
            for b in self.boutons_option:
                b.dessine()

        if self.indice_active:
            self.ecran.blit (self.indice,(80,100))

        pygame.display.update()
        self.timeur.tick(self.ips)
       


    def update (self):
        l = self.joueur.move()
        for i in range(2):
            if l[i] != None:
                self.niveau.portes.remove(l[i])
            if l[i+2] != None:
                self.niveau.cassables.remove(l[i+2])
        
        p = self.joueur.piece_collision()
        if p != None:
            self.niveau.pieces.remove(p)

        k = self.joueur.clef_collision()
        if k != None:
            self.niveau.clefs.remove(k)
        
        if self.joueur.victoire():
            return True


      

    def gestion_evenement (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            clefs = pygame.key.get_pressed()
            if clefs[pygame.K_LEFT]:
                self.joueur.deplacement_gauche = True
            if clefs[pygame.K_RIGHT]:
                self.joueur.deplacement_droit = True
    
            if clefs[pygame.K_SPACE]:
                if self.joueur.air_timeur < 10:
                    self.joueur.force_y = -11
            if event.type == pygame.KEYUP:
                if event.key == K_RIGHT:
                    self.joueur.deplacement_droit = False
                if event.key == K_LEFT:
                    self.joueur.deplacement_gauche = False
                
            if event.type == MOUSEBUTTONDOWN:
                if (not self.options_active) and (not self.indice_active):
                    for b in self.boutons:
                        if pygame.Rect.collidepoint(b.rect,event.pos):
                            res = b.clique()
                            if res == 0 :
                                self.indice_active = True
                            elif res == 1:
                                self.options_active = True

                elif self.options_active:
                    for b in self.boutons_option:
                        if pygame.Rect.collidepoint(b.rect,event.pos):
                            res = b.clique()
                            if res == 1:
                                return False
                            
                            elif res == 2:
                                self.options_active = False
                            elif res == 0:
                                print("sound disable for now !")

                elif self.indice_active:
                    self.indice_active = False
                
            if event.type == MOUSEMOTION:
                if (not self.options_active) and (not self.indice_active):
                    for b in self.boutons:
                        b.change_couleur(pygame.Rect.collidepoint(b.rect,event.pos))
                elif self.options_active:
                    for b in self.boutons_option:
                        b.change_couleur(pygame.Rect.collidepoint(b.rect,event.pos))
                

        
        

    def run (self):
        while self.running:
            res_events = self.gestion_evenement()
            if res_events != None:
                return res_events
            res_update = self.update()
            if res_update != None:
                return res_update

            self.affiche()
        
        

           

    def __str__(self):
        return "It's a menu bro !"

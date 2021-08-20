import pygame


class Joueur ():

    def __init__ (self, x, y, largeur, hauteur, ecran, niveau):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,largeur,hauteur)
        self.ecran = ecran
        self.couleur = pygame.Color("blue")
        self.deplacement = [0,0]
        self.vitesse = 5
        self.niveau = niveau
        
        self.saut_ok = False
        self.deplacement_droit = False
        self.deplacement_gauche = False
        self.force_y = 0
        self.air_timeur = 0
        self.cle = False

    def colls (self):
        cols = []
        porte = None
        cassable = None
    
        for rect in self.niveau.cubes_rects():
            if self.rect.colliderect(rect):
                cols.append(rect)
        d,etat = self.porte_collision()
        if d != None:
            cols.append(d.rect)
            if etat:
                porte = d
        b,etat = self.cassable_collision()
        if b != None:
            cols.append(b.rect)
            if etat:
                cassable = b

        return cols, porte, cassable

    def piece_collision (self):
        for p in self.niveau.pieces:
            if self.rect.colliderect(p.rect):
                return p
        return None

    def clef_collision (self):
        if not self.cle:
            for k in self.niveau.clefs:
                if self.rect.colliderect(k.rect):
                    self.cle = True
                    return k
        return None

    def porte_collision (self):
        for d in self.niveau.portes:
            if self.rect.colliderect(d.rect):
                if self.cle:
                    self.cle = False
                    return d,True
                return d, False
        return None, False

    #ici la tête du perso doit toucher
    def cassable_collision (self):
        for b in self.niveau.cassables:
            if pygame.Rect.collidepoint(b.rect, self.rect.midtop):
                print("hello collision break")
                return b, True
            elif self.rect.colliderect(b.rect):
                return b, False
                
        return None, False
        
        

            
    def victoire (self):
        if len(self.niveau.pieces) == 0:
            for z in self.niveau.zones:
                if self.rect.colliderect(z.rect):
                    return True
        return False
        
    def move (self):
        
        self.deplacement = [0,0]
        if self.deplacement_droit:
            self.deplacement[0] += 5
            
        if self.deplacement_gauche:
            self.deplacement[0] -= 5

        self.deplacement[1] += self.force_y
        self.force_y += 0.5
        if self.force_y > 7:
            self.force_y = 7


        collision_bas = False

        self.rect.x += self.deplacement[0]
        list_collision, porte, cassable = self.colls()
        
        for block in list_collision:
            if self.deplacement[0] > 0:
                self.rect.right = block.left
               
            elif self.deplacement[0] < 0:
                self.rect.left = block.right
            

        self.rect.y += self.deplacement[1]
        list_collision, porte2, cassable2 = self.colls()
        for block in list_collision:
            if self.deplacement[1] > 0:
                self.rect.bottom = block.top
                collision_bas = True
            elif self.deplacement[1] < 0:
                self.rect.top = block.bottom
                
        if collision_bas:
            self.force_y = 0
            self.air_timeur = 0
        else:
            self.air_timeur += 1

        return [porte,porte2, cassable,cassable2]


    def dessine (self):
        pygame.draw.rect (self.ecran, self.couleur,self.rect)

   

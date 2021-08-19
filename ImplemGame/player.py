import pygame
from level import Level

class Player ():

    def __init__ (self, x, y, width, height, screen, level):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,width,height)
        self.screen = screen
        self.color = pygame.Color("blue")
        self.velocity = [0,0]
        self.speed = 5
        self.level = level
        
        self.canJump = False
        self.deplacement_droit = False
        self.deplacement_gauche = False
        self.force_y = 0
        self.air_timer = 0
        self.cle = False

    def colls (self):
        cols = []
        door = None
        breakable = None
    
        for rect in self.level.cubes_rects():
            if self.rect.colliderect(rect):
                cols.append(rect)
        d,state = self.door_collision()
        if d != None:
            cols.append(d.rect)
            if state:
                door = d
        b,state = self.breakable_collision()
        if b != None:
            cols.append(b.rect)
            if state:
                breakable = b

        return cols, door, breakable

    def piece_collision (self):
        for p in self.level.pieces:
            if self.rect.colliderect(p.rect):
                return p
        return None

    def key_collision (self):
        if not self.cle:
            for k in self.level.keys:
                if self.rect.colliderect(k.rect):
                    self.cle = True
                    return k
        return None

    def door_collision (self):
        for d in self.level.doors:
            if self.rect.colliderect(d.rect):
                if self.cle:
                    self.cle = False
                    return d,True
                return d, False
        return None, False

    #ici la tête du perso doit toucher
    def breakable_collision (self):
        for b in self.level.breakables:
            if pygame.Rect.collidepoint(b.rect, self.rect.midtop):
                print("hello collision break")
                return b, True
            elif self.rect.colliderect(b.rect):
                return b, False
                
        return None, False
        
        

            
    def winning (self):
        if len(self.level.pieces) == 0:
            for z in self.level.zones:
                if self.rect.colliderect(z.rect):
                    return True
        return False
        
    def move (self):
        
        self.velocity = [0,0]
        if self.deplacement_droit:
            self.velocity[0] += 5
            
        if self.deplacement_gauche:
            self.velocity[0] -= 5

        self.velocity[1] += self.force_y
        self.force_y += 0.5
        if self.force_y > 7:
            self.force_y = 7

        collision_haut = False
        collision_bas = False
        collision_droite = False
        collision_gauche = False

        self.rect.x += self.velocity[0]
        list_collision, door, breakable = self.colls()
        
        for block in list_collision:
            if self.velocity[0] > 0:
                self.rect.right = block.left
                collision_droite = True
            elif self.velocity[0] < 0:
                self.rect.left = block.right
                collision_gauche = True

        self.rect.y += self.velocity[1]
        list_collision, door2, breakable2 = self.colls()
        for block in list_collision:
            if self.velocity[1] > 0:
                self.rect.bottom = block.top
                collision_bas = True
            elif self.velocity[1] < 0:
                self.rect.top = block.bottom
                collision_haut = True
                
        if collision_bas:
            self.force_y = 0
            self.air_timer = 0
        else:
            self.air_timer += 1

        return [door,door2, breakable,breakable2]

        

    def left (self):
        pass

            
            

    def jump (self):
        pass
        

    def draw (self):
        pygame.draw.rect (self.screen, self.color,self.rect)

   

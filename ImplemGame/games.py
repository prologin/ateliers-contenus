import sys, pygame
from pygame.locals import*
from button import Button
from utils import make_font, message_render
from level_maker import generate_level
from level import Level
from player import Player
import nextlevelmenu


class Game ():

    def __init__ (self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.timer = pygame.time.Clock()
        self.ips = 60
        self.running = True
        self.options_active = False
        self.hint_active = False
        self.buttons = [Button(24*self.width//25,self.height//15,"II",100,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda : 1,
                               self.screen),
                        Button(self.width//25,self.height//15,"H",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda  : 0,
                               self.screen),
        ]
        self.buttonsOption = [Button(21*self.width//25,self.height//15,"R",100,
                                     pygame.Color("white"),
                                     pygame.Color("red"),
                                     lambda  : 2,
                                     self.screen),
                              Button(17*self.width//25,self.height//15,"Q",100,
                                     pygame.Color("white"),
                                     pygame.Color("red"),
                                     lambda  : 1,
                                     self.screen),
                              Button(13*self.width//25,self.height//15,"S",100,
                                     pygame.Color("white"),
                                     pygame.Color("red"),
                                     lambda  : 0,
                                     self.screen),
        ]
        self.level, self.player = generate_level("3.txt", 40, self.screen)
        if self.player == None:
            raise ValueError("Le fichier du niveau ne contient pas de jouer")
        self.player.level = self.level
        
        self.hint_txt = f"Tu dois modifier dans le fichier player.py la fonction mouv"
        self.hint = message_render(self.hint_txt,make_font("BradBunR.ttf", 20),pygame.Color("black"))
            
            
    def display (self):
        self.screen.fill(pygame.Color("gray"))
      
        self.level.draw()

        self.player.draw()

        for b in self.buttons:
            b.draw()
            
        if self.options_active:
            for b in self.buttonsOption:
                b.draw()

        if self.hint_active:
            self.screen.blit (self.hint,(80,100))
       


    def update (self):
        l = self.player.move()
        for i in range(2):
            if l[i] != None:
                self.level.doors.remove(l[i])
            if l[i+2] != None:
                self.level.breakables.remove(l[i+2])
        
        p = self.player.piece_collision()
        if p != None:
            self.level.pieces.remove(p)

        k = self.player.key_collision()
        if k != None:
            self.level.keys.remove(k)

        """
        d = self.player.door_collision()
        if d != None:
            self.level.doors.remove(d)

            
        b = self.player.breakable_collision()
        if b != None:
            self.level.breakables.remove(b)
        """
       
        
        if self.player.winning():
            self.running = False
            nextlevelmenu.NextLevelMenu(self.width , self.height, self.screen).run()

        
            
      

    def handling_events (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.deplacement_gauche = True
            if keys[pygame.K_RIGHT]:
                self.player.deplacement_droit = True
    
            if keys[pygame.K_SPACE]:
                if self.player.air_timer < 10:
                    self.player.force_y = -11
            if event.type == pygame.KEYUP:
                if event.key == K_RIGHT:
                    self.player.deplacement_droit = False
                if event.key == K_LEFT:
                    self.player.deplacement_gauche = False
                
            if event.type == MOUSEBUTTONDOWN:
                if (not self.options_active) and (not self.hint_active):
                    for b in self.buttons:
                        if pygame.Rect.collidepoint(b.rect,event.pos):
                            res = b.on_click()
                            if res == 0 :
                                self.hint_active = True
                            elif res == 1:
                                self.options_active = True
                elif self.options_active:
                    for b in self.buttonsOption:
                        if pygame.Rect.collidepoint(b.rect,event.pos):
                            res = b.on_click()
                            if res == 1:
                                self.running = False
                            elif res == 2:
                                self.options_active = False
                            elif res == 0:
                                print("sound disable for now !")
                elif self.hint_active:
                    self.hint_active = False
                
            if event.type == MOUSEMOTION:
                if (not self.options_active) and (not self.hint_active):
                    for b in self.buttons:
                        b.change_col(pygame.Rect.collidepoint(b.rect,event.pos))
                elif self.options_active:
                    for b in self.buttonsOption:
                        b.change_col(pygame.Rect.collidepoint(b.rect,event.pos))
                

        
        

    def run (self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            
         
            pygame.display.update()
            self.timer.tick(self.ips)

           

    def __str__(self):
        return "It's a menu bro !"

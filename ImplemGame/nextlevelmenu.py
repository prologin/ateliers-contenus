import sys, pygame
from pygame.locals import*
from button import Button
import games
from utils import make_font



class NextLevelMenu ():

    def __init__ (self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.timer = pygame.time.Clock()
        self.ips = 60
        self.running = True
        self.buttons = [Button(self.width//2,self.height//4,"Prochain niveau!",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda :  games.Game(self.width, self.height, self.screen).run(),
                               self.screen),
                        Button(self.width//2,2*self.height//4,"Options!",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda : True,
                               self.screen),
                        Button(self.width//2,3*self.height//4,"Quitter!",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda : False,
                               self.screen),
        ]
            
            
    def display (self):
        self.screen.fill(pygame.Color("gray"))
        for b in self.buttons:
            b.draw()
       


    def update (self):
        pass

    def handling_events (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            if event.type == MOUSEBUTTONDOWN:
                
                for b in self.buttons:
                    if pygame.Rect.collidepoint(b.rect,event.pos):
                        res = b.on_click
                        if not res:
                            self.running = False
                    
            if event.type == MOUSEMOTION:
                for b in self.buttons:
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





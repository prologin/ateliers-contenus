import sys, pygame
from pygame.locals import*
from button import Button
from games import Game
from utils import make_font



class MainMenu ():

    def __init__ (self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.timer = pygame.time.Clock()
        self.ips = 60
        self.running = True
        self.buttons = [Button(self.width//2,self.height//4,"Jouer!",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda : Game(self.width, self.height, self.screen).run(),
                               self.screen),
                        Button(self.width//2,2*self.height//4,"Options!",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda : print("sad!"),
                               self.screen),
                        Button(self.width//2,3*self.height//4,"Quitter!",80,
                               pygame.Color("white"),
                               pygame.Color("red"),
                               lambda : quit(),
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
                        b.on_click()
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





if __name__ == '__main__':

    pygame.init()

    width, height = 1200 , 800

    screen = pygame.display.set_mode((width, height))
    menu = MainMenu(width,height,screen)
    menu.run()

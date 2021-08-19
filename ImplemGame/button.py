from utils import message_render, make_font
import pygame

class Button ():
    
    def __init__ (self, x, y, txt, size, col1, col2, func, screen):
        self.screen = screen
        self.txt = txt
        self.size = size
        self.mess = message_render(txt,make_font("BradBunR.ttf", self.size),col1)
        self.width = self.mess.get_width()
        self.height = self.mess.get_height()

        self.coords = (x-(self.width//2),y-(self.height//2))
        self.rect = pygame.Rect(self.coords[0], self.coords[1], self.width, self.height)
        self.cols = [col1,col2]
        self.func = func

    def change_col (self, state):
        self.mess = message_render(self.txt, make_font("BradBunR.ttf", self.size),
                                   self.cols[1] if state else self.cols[0])

    def on_trigger (self):
        self.change_col (True)
    
        

    def on_click (self):
        return self.func()

    def draw (self):
        self.screen.blit (self.mess,self.coords)






        

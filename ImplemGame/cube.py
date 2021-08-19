import pygame


class Cube ():

    def __init__ (self, x, y, width, height, screen):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,width,height)
        self.mini_rect = pygame.Rect(x+(width//10),y+(height//10),width-(width//5),height-(height//5))
        self.screen = screen
        self.color = pygame.Color("black")
        self.mini_color = pygame.Color("grey39")

    def draw (self):
        pygame.draw.rect (self.screen, self.color,self.rect)
        pygame.draw.rect (self.screen, self.mini_color,self.mini_rect)

class Coin ():
    def __init__ (self, x, y, width, height, screen):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,width,height)
        self.screen = screen
        self.color = pygame.Color("yellow")
        
    def draw (self):
        pygame.draw.rect (self.screen, self.color,self.rect)

class WinningZone ():
    def __init__ (self, x, y, width, height, screen):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,width,height)
        self.screen = screen
        self.color = pygame.Color("green")

    def draw (self):
        pygame.draw.rect (self.screen, self.color,self.rect)

class Door ():
    def __init__ (self, x, y, width, height, screen):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,width,height)
        self.screen = screen
        self.color = pygame.Color("brown")

    def draw (self):
        pygame.draw.rect (self.screen, self.color,self.rect)

class Key ():

    def __init__ (self, x, y, width, height, screen):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,width,height)
        self.mini_rect = pygame.Rect(x+(width//10),y+(height//10),width-(width//5),height-(height//5))
        self.screen = screen
        self.color = pygame.Color("black")
        self.mini_color = pygame.Color("yellow")

    def draw (self):
        pygame.draw.rect (self.screen, self.color,self.rect)
        pygame.draw.rect (self.screen, self.mini_color,self.mini_rect)


class Breakable ():

    def __init__ (self, x, y, width, height, screen):
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect(x = x, y = y)
        self.rect = pygame.Rect(x,y,width,height)
        self.mini_rect = pygame.Rect(x+(width//10),y+(height//10),width-(width//5),height-(height//5))
        self.screen = screen
        self.color = pygame.Color("black")
        self.mini_color = pygame.Color("brown")

    def draw (self):
        pygame.draw.rect (self.screen, self.color,self.rect)
        pygame.draw.rect (self.screen, self.mini_color,self.mini_rect)

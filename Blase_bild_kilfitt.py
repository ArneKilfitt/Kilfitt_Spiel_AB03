import pygame                                           # Stellt Objekte und Konstanten zur Spielprogrammierung zur Verfügung
from pygame.constants import (QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_LEFT, K_RIGHT,K_SPACE,K_KP_MINUS,K_KP_PLUS,K_F10,K_BACKSPACE)
import random
import os

class Settings(object):

  

    test = 10
    width = 500                            # Hier wird das Fenster defieniert 
    height = 500
    fps = 60     
    title = "Test"   
    file_path = os.path.dirname(os.path.abspath(__file__)) # Hier wird auf der ordner hingewiesen  
    images_path = os.path.join(file_path, "images")   # in dem sich die bilder befinden 
    def get_dim(self):
        return (self.width, self.height) 





class Kreis(pygame.sprite.Sprite):  
    def __init__(self, settings,xg):
        pygame.sprite.Sprite.__init__(self)
        self.xg = xg 
        self.wachstum = 0 
        self.settings = settings
        self.image = pygame.image.load(os.path.join(self.settings.images_path, "kreis3.png")).convert_alpha()  # katzen bild wird geladen 
        self.image = pygame.transform.scale(self.image, (self.xg,self.xg))           # große der katze 
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(20,settings.width-20-self.rect.width)  
        self.rect.top =  random.randint(20,settings.height-20-self.rect.height)       

    
  
    






        




class Game(object):

    #zuhname = randint(1,4)
    def __init__(self, pygame, settings):
        self.pygame = pygame
        self.settings = settings
        self.screen = pygame.display.set_mode(settings.get_dim())
        self.pygame.display.set_caption(self.settings.title)
        self.background = self.pygame.image.load(os.path.join(self.settings.images_path, "background2.png")).convert()
        self.background_rect = self.background.get_rect()
       # self.kreis = self.pygame.image.load(os.path.join(self.settings.images_path,"kreis3.png")).convert()
       # self.kreis_rect = self.background.get_rect()
        self.all_kreise = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.done = False
        







    def run(self):
        while not self.done:                            # Hauptprogrammschleife mit Abbruchkriterium   
            self.clock.tick(self.settings.fps)          # Setzt die Taktrate auf max 60fps   
            for event in self.pygame.event.get():       # Durchwandere alle aufgetretenen  Ereignisse
                if event.type == QUIT:                  # Wenn das rechts obere X im Fenster geklickt
                    self.done = True                    # Flag wird auf Ende gesetzt
                elif event.type == KEYDOWN:             # Reagiere auf Taste drücken
                    if event.key == K_ESCAPE:
                        self.done = True


            self.update()
        
            self.draw()
    
          #  Game.kreis()
 
    def draw(self):
        self.screen.blit(self.background, self.background_rect)
        self.all_kreise.draw(self.screen)
       # self.screen.blit(self.kreis,self.kreis_rect)
       # self.screen.blit(self.kreis,self.kreis_rect)
        self.pygame.display.flip()   # Aktualisiert das Fenster

    
    def kreis():

        self.screen.blit(self)

    def update(self):
        if Settings.test <= 50 :
            self.all_kreise.add(Kreis(self.settings,Settings.test))
            Settings.test = Settings.test + random.randint(1,4)
        




if __name__ == '__main__':      
                                    
    settings = Settings()       

    pygame.init()              

    game = Game(pygame, settings)
    game.run()
  

    pygame.quit()               






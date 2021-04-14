import pygame                                          
import os
from pygame.locals import *
from pygame.constants import (QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_LEFT, K_RIGHT,K_SPACE,K_KP_MINUS,K_KP_PLUS,K_F10,K_BACKSPACE)
import random
print("test")  
pygame.init()


class Settings(object):       
  file_path = os.path.dirname(os.path.abspath(__file__)) # Hier wird auf der ordner hingewiesen  
  images_path = os.path.join(file_path, "images")   # in dem sich die bilder befinden 
  
  bitmap = pygame.image.load(os.path.join(images_path, "kreis2.png"))
  kreis = bitmap.get_rect()

  fps = 60
  size = [700, 500]
  screen = pygame.display.set_mode(size)
  clock = pygame.time.Clock()

  weiss = [255,255,255]
  rot = [255,0,0]
  braun = [139,69,0]
  braun2 = [139,69,19]
  grau = [139,136,120]
  gruen = [0,100,0]
  gruen2 = [0,201,87]
  gruen3 = [50,205,50]

  randx = 700
  randy = 500
  zeit = 0
  start = False
  erzeug = True 

  all_kreise = pygame.sprite.Group()






class Game(pygame.sprite.Sprite):
  class Game(object):
    def __init__(self, pygame, settings):
        self.pygame = pygame
        self.settings = settings

       

        self.katze = Cat(settings)
        self.clock = pygame.time.Clock()
        self.done = False
        
        self.cat_1 = pygame.sprite.Group()
        self.cat_1.add(self.katze)









    def draw(self):
        self.screen.blit(self.background, self.background_rect)
        self.cat_1.draw(self.screen)
        self.pygame.display.flip()   # Aktualisiert das Fenster





  def erzeug():
    if Settings.erzeug == True :
      for i in range(10):
        Game.draw()
        Settings.erzeug = False 








class Kreis(pygame.sprite.Sprite):



  def __init__(self,x0,y0,xg,bscreen):
    pass




class Maus(pygame.sprite.Sprite):
  
  test = 0





 

    #(random.randint(100,300))
    #self.y0 = self.y0 - 0.1 
    #self.x0 = self.x0 - 0.1
    #self.xx1 = self.xx1 + 0.2





 


# Speichert ob das Spiel-Fenster geschlossen wurde
done = False

while not done:
  Settings.clock.tick(60)
  pygame.display.flip()
  Game.erzeug()




  #for maus in all_maus:
    #t = pygame.sprite.collide_mask()
  

            








  #kk = pygame.sprite.spritecollide(kreis,)








  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True



    
    







#pygame.QUIT()






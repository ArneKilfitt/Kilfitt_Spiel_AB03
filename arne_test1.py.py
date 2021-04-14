import pygame                                          
import os
from pygame.locals import *
from pygame.constants import (QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_LEFT, K_RIGHT)
import random
print("test")   
pygame.init()
class Settings(object): 
  fps = 60        
  file_path = os.path.dirname(os.path.abspath(__file__)) # Hier wird auf der ordner hingewiesen  
  images_path = os.path.join(file_path, "images")   # in dem sich die bilder befinden 
  
  bitmap = pygame.image.load(os.path.join(images_path, "alienbig0302.png"))
  bildgroessen = bitmap.get_rect()

  fps = 60

  weiss = [255,255,255]
  rot = [255,0,0]
  braun = [139,69,0]
  braun2 = [139,69,19]
  grau = [139,136,120]
  gruen = [0,100,0]
  gruen2 = [0,201,87]
  gruen3 = [50,205,50]







  


class Blocke(pygame.sprite.Sprite) :
  def __init__(self,blockx,blocky,block_farbe,block_screen):
      #  pygame.sprite.Sprite.__init__(self)
    self.x = blockx
    self.y = blocky
    self.block_farbe = block_farbe
    self.screen = self.block_screen



class Game():
  def __init__(self,x0,y0,xx1,bscreen):
    self.screen = bscreen 
    self.x0 = 0    
    self.y0 = 0   
    self.xx1 = 10                                                # Dicke
    self.xx2 = 10    
    self.xx7 = 10                                                # größe (also wie viel ist vom kreis lerr)
#(random.randint(100,300))
  def reihe1(self):
    pygame.draw.ellipse(self.screen, Settings.rot, [self.x0+100,self.y0+100,self.xx1,self.xx1], 10)
    self.xx1 = self.xx1 + 0.2
    self.x0 = self.x0 -0.1
    self.y0 = self.y0 -0.1








    
  def update():
    #Game.zeichnen()
    blase1.reihe1()








size = [700, 500]
screen = pygame.display.set_mode(size)

blase1 = Game(200,200,10,screen)
blase2 = Game(100,200,10,screen)
blase3 = Game(100,300,10,screen)
blase4 = Game(200,100,10,screen)
blase5 = Game(200,300,10,screen)
blase6 = Game(200,400,10,screen)
blase7 = Game(300,100,10,screen)
# Noetig um die fps zu begrenzen
clock = pygame.time.Clock()

# Speichert ob das Spiel-Fenster geschlossen wurde
done = False

while not done:
  clock.tick(60)
  pygame.display.flip()
  Game.update()
  
  
  
  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True



    
    







#pygame.QUIT()






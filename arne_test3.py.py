import pygame                                          
import os
from pygame.locals import *
from pygame.constants import (QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_LEFT, K_RIGHT,K_SPACE,K_KP_MINUS,K_KP_PLUS,K_F10)
import random
print("test")   
x = 0
pygame.init()


class Settings(object):       
  file_path = os.path.dirname(os.path.abspath(__file__)) # Hier wird auf der ordner hingewiesen  
  images_path = os.path.join(file_path, "images")   # in dem sich die bilder befinden 
  
  bitmap = pygame.image.load(os.path.join(images_path, "alienbig0302.png"))
  bildgroessen = bitmap.get_rect()

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
  wertx = 0
  werty = 0
  wertd = 0
  wertv = 10


  def erzeug():
    if Settings.erzeug == True :
      for i in range(10):
        Kreis.kreis_printen()

        Settings.erzeug = False 


    else :
        pass

#if not pygame.sprite.spritecollide(kreis,Settings.all_kreise,False) :




class Kreis(pygame.sprite.Sprite):



  def __init__(self,x0,y0,xg,bscreen):
    self.screen = bscreen 
    self.x0 = x0  
    self.y0 = y0  
    self.xg = xg                                             # goße                                             # fullung
    self.x1 = x0 + xg/2 - 1/2
    self.y1 = y0 + xg/2 - 1/2  
    self.rect = 100
  def kreis_zeichnen(self):
    pygame.draw.ellipse(self.screen, Settings.rot, [self.x0,self.y0,self.xg,self.xg],1000)
    pygame.draw.ellipse(self.screen, Settings.weiss, [self.x1,self.y1,1,1],1)


  def initialisiere_kreis():
    kreis = Kreis(Kreis.gib_random_x0(),Kreis.gib_random_y0(),10,Settings.screen)
    return kreis 

  def kreis_printen():
    kreis = Kreis.initialisiere_kreis()
    kreis.kreis_zeichnen()



  def gib_random_x0():
    random_x0 = random.randint(10,Settings.randx-20)
    return random_x0
  def gib_random_y0():
    random_y0 = random.randint(10,Settings.randy-20)
    return random_y0






 

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




  #kk = pygame.sprite.spritecollide(kreis,)








  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True



    
    







#pygame.QUIT()






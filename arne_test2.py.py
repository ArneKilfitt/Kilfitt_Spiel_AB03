import pygame                                          
import os
from pygame.locals import *
from pygame.constants import (QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_LEFT, K_RIGHT,K_SPACE,K_KP_MINUS,K_KP_PLUS,K_F10)
import random
print("test")   
pygame.init()
x = 0

class Settings(object):       
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

  randx = 700
  randy = 500
  zeit = 0
  wertx = 0
  werty = 0
  wertd = 0
  wertv = 10
  start = False









  


#class Blocke(pygame.sprite.Sprite) :
 # def __init__(self,blockx,blocky,block_farbe,block_screen):
  #    #  pygame.sprite.Sprite.__init__(self)
   # self.x = blockx
   # self.y = blocky
   # self.block_farbe = block_farbe
   # self.screen = self.block_screen


class Kreis():
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def gib_x(self):
    print("test")
    return x 
class Game():
  def __init__(self,x0,y0,xx1,bscreen):
    self.screen = bscreen 
    self.x0 = x0  
    self.y0 = y0  
    self.xx1 = xx1                                              # Dicke
    self.xx2 = 10    
    self.xx7 = 10 
               # größe (also wie viel ist vom kreis lerr)
#(random.randint(100,300))

  def reihe1(self):
    pygame.draw.ellipse(self.screen, Settings.rot, [self.x0,self.y0,self.xx1,self.xx1], 10)
    self.y0 = self.y0 - 0.1 
    self.x0 = self.x0 - 0.1
    self.xx1 = self.xx1 + 0.2
    print(self.xx1)
  def blase():
    #print(Settings.zeit)
    pass


  def zeichnen():
    #if Settings.start == False: 
 
    random1 = random.randint(10,Settings.randx-20)
    random2 = random.randint(10,Settings.randy-20) 
    pygame.draw.ellipse(screen,Settings.rot,[Settings.wertx + random1,Settings.werty + random2 ,Settings.wertd + 10,Settings.wertd + 10],1000)
    #  print(random1,random2)
    #  random1_neu = random.randint(10,Settings.randx-20)
     # random2_neu = random.randint(10,Settings.randy-20)
     # Settings.start = True
      #  if Settings.start == True :
       #   pass
      
      #pygame.draw.ellipse(screen,Settings.rot,[Settings.wertx + random1,Settings.werty + random2 ,Settings.wertd + 10,Settings.wertd + 10],1000)     





  def update():
    Settings.wertx = Settings.wertx - 0.1
    Settings.werty = Settings.werty - 0.1
    Settings.wertd = Settings.wertd + 0.2





      

    
  def update2():

    if Settings.zeit > 0 :
      blase1.reihe1()

    if Settings.zeit > 100 :
      blase2.reihe1()

    if Settings.zeit > 200 :
      blase3.reihe1()
    if Settings.zeit > 300 :
      blase4.reihe1()




 



size = [700, 500]
screen = pygame.display.set_mode(size)
blase1 = Game(random.randint(10,Settings.randx-20),random.randint(10,Settings.randy-20),10,screen) # 10 um den Abstand vo nrand auf 10 zu setzen und 20 weil noch die breite vom objet 10 da zu kommt 
blase2 = Game(200,200,10,screen)
blase3 = Game(300,300,10,screen)
blase4 = Game(300,200,10,screen)
random1 = 0
random2 = 0




#kreis1 = Kreis(10,100)









# Noetig um die fps zu begrenzen
clock = pygame.time.Clock()

# Speichert ob das Spiel-Fenster geschlossen wurde
done = False

while not done:
  clock.tick(60)
  pygame.display.flip()

 # Game.update2()
  Game.update2()
  Game.blase()
  Settings.zeit = Settings.zeit + 1 
  #kreis1 = Kreis(10,100)
  a = int
  a = 0
 # a = Kreis.gib_x()
  print(a)
 

  #Game.zeichnen()


 # pygame.Game.spritecollide()
  
  
  
  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True



    
    







#pygame.QUIT()






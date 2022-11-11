#hello! how are you?


import pygame
from makoto import *
from angstyteen import *
from TroubleMaker import *
from arsonist import *
from bear import *
from survivor import *
from assassin import *
from detective import *
from boydetective import*
from soldier import *
from GamerGod import*
from Nurse import*
#from variables import *

pygame.init()  # initalizes Pygame
pygame.display.set_caption("Danganronpa")  # sets the window title
Hajime0 = pygame.image.load('sprites/IMG_7769.PNG')
Hajime1 = pygame.image.load('sprites/IMG_7770.PNG')
Nagito1 = pygame.image.load('sprites/Nagito.PNG')
Nagito0 = pygame.image.load('sprites/Nagit0.PNG')
font= pygame.font.Font('freesansbold.ttf',32)
font1 = pygame.font.Font('freesansbold.ttf',12)

good = font.render("good job you escaped!", True, (0,0,0))
good1 = font.render("thanks for playing!", True, (0,0,0))
credit = font.render("sprites by spike chunsoft", True, (0,0,0))
screen = pygame.display.set_mode((500, 500))  # creates game screen 
clock = pygame.time.Clock()# start game clock
#game varialbles---------------------------------------------
doExit = False #this variable controls our game loop
playerX = 450 #player x position
playerY = 380 #player y position
isOnGround = False 
Vx = 0 #player left/right speed
Vy = 0 #player up/down speed
direction = 1
ticker = 0
days = 1
day = True
counter = 0
codes = 0#Nagitos method of escape
key1 = True
key2 = True
key3 = True
roomkey = True
hope = 0#hajimes method of escape
#blink = 0
IK = 120#izuru x position
KO = 10#Kokichi x position
mono = 300 # monokuma xpos
RA = 100#rantaro xpos
NK = 235#NPC nagito x position
MN = 100#makoto x position
MH = 60#maki xpos
MI = 40#mukuro xpos
MT = 90#Mikan xpos
CN = 340#Chiaki xpos
SS = 150#shuichi xpos
KK = 160#kyoko xpos
comy = 380#I figured that most of the NPC's could share a ypos because they wont be moving
location = 0
#limiting the amount of hope fragments a character can give
kamakura = 3
oma = 3
amami = 3
komaeda = 3
naegi = 3
harukawa = 3
ikusaba = 3
tsumiki = 3
nanami = 3
saihara = 3
kirigiri = 3

#game loop#######################################
while not doExit:
    clock.tick(60)
#physics section-----------------------------
    #lets you quit the game from the gamescreen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
   
    # input/output section
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Vx = -2
        direction = 1
        ticker+= 1
        if ticker > 5:
          ticker = 0
          counter+=1
          if counter>1:
            counter = 0
    elif keys[pygame.K_RIGHT]:
        Vx = 2
        direction = 0
        ticker+= 1
        if ticker > 5:
          ticker = 0
          counter+=1
          if counter>1:
            counter = 0
    elif keys[pygame.K_SPACE] and day is False:
        if isOnGround == True: #comment this to ensable double jumping
            Vy = -5
    else:
      counter = 0

    playerX += Vx
    playerY += Vy
    

    #GRAVITY
    if playerY > 400 - 20 and location != 5: #check if your feet are on the ground
        isOnGround = True
        playerY = 400 - 20
        Vx = 0 #stot falling if on ground
    else:
        isOnGround = False
        counter = 1


    
      


    #animation
    if day is True or day is False:
      tick+=1
      if tick>30:
        tick = 0
        blink+=1
        blink2 +=1
        if blink>3:
          blink = 0
        if blink2>1:
          blink2=0


    if isOnGround == False:
        Vy+=.2 #if not on ground, fall downwards

    #locations
    if location == 0 and playerX < 0:#going left
      location = 1
      playerX = 450
    if location == 1 and playerX > 500:#going right
      location = 0
      playerX = 40
    if location == 1 and playerX < 0:#going left
      location = 2
      playerX = 450
    if location == 2 and playerX > 500:#going right
      location = 1
      playerX = 40
    if location ==2 and playerX < 0:
      location = 5
      playerX = 450
    if location == 3 and playerX > 500:
      location = 2
      playerX = 40
    if location == 5 and playerX < 400 and playerY == 380:
      location = 3
    if location == 3 and playerX > 400:
      location = 5
    if playerY > 500:
      location = 4
      playerY = 20
      playerX = 450
    if location == 4 and playerX < 20:
      location = 0
      playerY = 250
      playerX = 250
    if location == 3 and playerX < 0:
      location = 9
      playerX = 450
    if location == 9 and playerX > 500:
      location = 3
      playerX = 40


    #indoor locations
    if location == 1 and playerX > 210 and playerX < 360:#first house
      if keys[pygame.K_UP]:
        location = 6
        playerX = 450
    if location == 6 and playerX > 500:
      location = 1
      playerX = 280
    if location == 6 and playerX < 0:#2nd room of first house
      location = 7
      playerX = 450
    if location == 7 and playerX > 500:
      location = 6
      playerX = 40
    if location == 2:
      if keys[pygame.K_UP] and playerX >= 190 and playerX <= 190+ 120:#hatch room
        location = 8
        playerX = 450
    if location == 8 and playerX > 500:
      location = 2
      playerX = 255
    if location == 8 and playerX > 210 and playerX < 360:#escape
      if keys[pygame.K_UP] :
        if codes == 3 or hope == 20:
          location = 100
          playerX = 450
    if location == 9 and playerX > 210 and playerX < 360:#abandoned house
      if keys[pygame.K_UP]:
        location = 10
        playerX = 450
    if location == 10 and playerX > 500:
      location =9
      playerX = 280
    if location == 10 and playerX >= 150 and playerX <= 210 and roomkey is False:#locked room in abandoned house
      if keys[pygame.K_UP]:
        location = 11
        playerX = 450
    if location == 11 and playerX > 500:
      location = 10
      playerX = 180


    #barriers
    if location == 9 and playerX < 0:
      playerX = 1
    if location == 7 and playerX < 0:
      playerX = 1
    if location == 4 and playerX > 500:
      playerX = 497
    if location == 8 and playerX < 0:
      playerX = 1
    if location == 10 and playerX < 0:
      playerX = 1
    if location == 11 and playerX < 0:
      playerX = 1
    

    #changing from day to night
    if location == 0 and playerX > 500 and day is True:
      day = False
      playerX = 450
      direction = 1
    if location == 0 and playerX > 500 and day is False:
      day = True
      playerX = 450
      direction = 1
      days += 1

    #obtaining keys
    if location == 0 and day is False and playerX >=260 and playerX <= 300 and key1 is True:
      if keys[pygame.K_UP]:
        codes += 1
        key1 = False
    if location == 7 and day is False and playerX >= MH and playerX <= 160 and key2 is True:
      if keys[pygame.K_UP]:
        codes += 1
        key2 = False
    if location == 4 and day is False and playerX >= IK and playerX <= 220 and roomkey is True:
      if keys[pygame.K_UP]:
        roomkey = False
    if location == 11 and playerX >= 70 and playerX <= 180 and day is False and key3 is True:
      if keys[pygame.K_UP]:
        codes += 3
        key3 = False

    
#render section-------------------------------
    if day is False:
      screen.fill((76, 64, 142)) #clear screen between loops
    
    if day is True:
      screen.fill((135,206,235))
    #pygame.draw.rect(screen, (255, 50, 50), (playerX, playerY, 20, 20)) #draw player

    if location == 1:
      pygame.draw.rect(screen, (87,89,93), (210, 300, 150
      ,100))#base house
      pygame.draw.rect(screen, (101, 67, 33), (270, 340, 40
      ,60))#door
      pygame.draw.rect(screen, (165,42,42), (230, 230, 20
      ,60))#chimney
      pygame.draw.polygon(screen, (0,0,0), ((200, 300), (370, 300), (285, 240)))#roof
      pygame.draw.ellipse(screen, (192,192,192), (210, 220, 20, 10))
      pygame.draw.ellipse(screen, (192,192,192), (190, 210, 25, 15))
      pygame.draw.ellipse(screen, (192,192,192), (170, 200, 30, 20))#smoke clouds
      if day is True:
        screen.blit(Mukuro0, (MI,comy - 63 ), (0+blink*51,0,51,100))
        screen.blit(Mikan0, (MT,comy - 63 ), (0+blink*81,0,80,100))


    if location == 10 or location == 11:
      pygame.draw.rect(screen, (43,45,47), (0, 0, 500, 500))
    if location == 10:
      pygame.draw.rect(screen, (101, 67, 33), (150, 320, 60
      ,80))
    if location == 11:
      pygame.draw.rect(screen, (101, 67, 33), (70, 360, 80,40))


    if location == 9:
      pygame.draw.rect(screen, (54,34,4), (210, 300, 150
      ,100))#base house
      pygame.draw.rect(screen, (0, 0, 0), (270, 340, 40
      ,60))#door
      
      pygame.draw.polygon(screen, (0,0,0), ((200, 300), (370, 300), (285, 240)))#roof

    if location == 2:
      
      pygame.draw.rect(screen, (0,0,0), (100, 200, 300, 200))
      pygame.draw.rect(screen, (255,255,255), (190, 320, 120, 80))
      if day is False:
        screen.blit(Monokuma0, (mono,comy - 58), (0+blink2*55,0,57,100))

    if location == 8:
      pygame.draw.rect(screen, (255,255,255), (0, 0, 500, 500))
      pygame.draw.circle(screen, (130, 135, 136), (255, 250), 130)
      pygame.draw.rect(screen, (130,135,136), (110, 200, 20,100))
      pygame.draw.rect(screen, (0,0,0), (220, 230, 80,80))
      if day is True:
        screen.blit(Rantaro0, (RA,comy - 75 ), (0+blink*66,0,65,100))

    
    if location == 6 or location == 7:
      pygame.draw.rect(screen, (87,89,93), (0, 0, 500, 500))#wall paper
    if location == 6:
      pygame.draw.rect(screen, (155,103,60), (80, 350, 125, 10))
      pygame.draw.rect(screen, (155,103,60), (80, 350, 10, 50))
      pygame.draw.rect(screen, (155,103,60), (205, 350, 10, 50))#table
      screen.blit(Kokichi0, (KO,comy - 64 ), (0+blink*69,0,68,100))
      if day is True:
        screen.blit(Nagito3, (NK,comy - 78), (0+blink*81,0,80,100))
        screen.blit(Chiaki0, (CN,comy - 64 ), (0+blink*75,0,68,100))

    if location == 7:
      screen.blit(Maki0, (MH,comy - 64), (0+blink*75,0,75,100))
      if day is True:
        screen.blit(Shuichi0, (SS,comy - 75), (0+blink*60,0,60,100))

    if location == 4:
      pygame.draw.rect(screen, (0,0,0), (0, 0, 500, 500))
      pygame.draw.rect(screen, (78,115,223), (40, 300, 40, 300))#portal pt 1
      screen.blit(Izuru0, (IK,comy - 75 ), (0+blink*75,0,75,100))
    

    #Makoto(MN,comy )
    if location == 0 and day is True:
      screen.blit(Makoto0, (MN,comy - 78), (0+blink*63,-5,60,100))
      screen.blit(Kyoko0, (KK,comy - 69), (0+blink*72,-5,70,100))
    if location == 0:#apartment complex
      pygame.draw.rect(screen, (165,42,42), (270, 30, 230
      ,400))
      pygame.draw.rect(screen, (0,0,0), (300, 70, 40
      ,60))#window column 1
      pygame.draw.rect(screen, (0,162,237), (360, 70, 40
      ,60))#window column 2
      pygame.draw.rect(screen, (0,162,237), (420, 70, 40
      ,60))#window column 3
      pygame.draw.rect(screen, (0,162,237), (300, 160, 40
      ,60))#window column 1
      pygame.draw.rect(screen, (0,162,237), (360, 160, 40
      ,60))#window column 2
      pygame.draw.rect(screen, (0,0,0), (420, 160, 40
      ,60))#window column 3
      pygame.draw.rect(screen, (0,162,237), (300, 250, 40
      ,60))#window column 1
      pygame.draw.rect(screen, (0,0,0), (360, 250, 40
      ,60))#window column 2
      pygame.draw.rect(screen, (0,0,0), (420, 250, 40
      ,60))#window column 3
      pygame.draw.rect(screen, (0,0,0), (300, 330, 40
      ,60))#window column 1
      pygame.draw.rect(screen, (0,162,237), (360, 330, 40
      ,60))#window column 2
      pygame.draw.rect(screen, (0,162,237), (420, 330, 40
      ,60))#window column 3
      pygame.draw.rect(screen, (0,0,0), (470, 320, 30
      ,80))#door


    if direction == 0 and day is True:
      screen.blit(Hajime0, (playerX-20,playerY - 80), (0+counter*55,-5,55,100))
    if direction == 1 and day is True:
      screen.blit(Hajime1, (playerX-20,playerY - 80), (0+counter*55,-5,55,100))
    if direction == 0 and day is False:
      screen.blit(Nagito0, (playerX-25,playerY - 80), (0+counter*80,0,84,100))
    if direction == 1 and day is False:
      screen.blit(Nagito1, (playerX-20,playerY - 80), (0+counter*80,0,84,100))

    if location != 3 or location != 4:
      pygame.draw.rect(screen, (119,136,153), (0, 400, 500, 100)) # sidewalk
    if location == 3 or location == 5:
      pygame.draw.rect(screen, (119,136,153), (0, 400, 400, 100))
      pygame.draw.rect(screen, (0,0,0), (400, 400, 100, 100))
    if location == 4:
      
      
      pygame.draw.rect(screen, (78,115,223), (0, 300, 40, 300))#portal pt 2
      pygame.draw.rect(screen, (0,0,0), (0, 400, 500, 100))
  
    if location == 8:
      pygame.draw.rect(screen, (0,0,0), (0, 400, 500, 100))

    if location == 6 or location == 7:
      pygame.draw.rect(screen, (101, 67, 33), (0, 400, 500, 100))#wood floor

    if location == 10 or location == 11:
      pygame.draw.rect(screen, (54,34,4), (0, 400, 500, 100))

    if location == 100:
      pygame.draw.rect(screen, (255,255,255), (0, 0, 500, 500))
      screen.blit(good, (0,0))
      screen.blit(good1, (0,40))
      screen.blit(credit, (0,80))

    
    if days == 41:
      pygame.draw.rect(screen, (0,0,0), (0, 0, 500, 500))


    #text
    #Izuru
    if location == 4 and day is True and playerX >= IK and playerX <= IK + 100:
      if keys[pygame.K_UP]:
        if kamakura == 3:
          screen.blit(Iktxt1, (50, 420))
          screen.blit(Iktxt2, (50, 435))
          hope += 1
    #Nagito
    if location == 6 and day is True and playerX >= NK and playerX <= NK + 100:
      if keys[pygame.K_UP]:
        if komaeda == 3:
          screen.blit(Nktxt1, (50, 420))
          screen.blit(Nktxt2, (50, 435))
          hope += 1
    #Chiaki
    if location == 6 and day is True and playerX >= CN and playerX <= CN + 100:
      if keys[pygame.K_UP]:
        if nanami == 3:
          screen.blit(Cntxt1, (50, 420))
          screen.blit(Cntxt2, (50, 435))
          hope += 1
    #Kokichi
    if location == 6 and day is True and playerX >= KO and playerX <= KO + 100:
      if keys[pygame.K_UP]:
        if oma == 3:
          screen.blit(Kotxt1, (50, 420))
          screen.blit(Kotxt2, (50, 435))
          hope += 1

    pygame.display.flip() #draws all the stuff above the screen    
    
#####################################end game loop
pygame.quit()


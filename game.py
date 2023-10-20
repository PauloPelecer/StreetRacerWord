import pygame
import time, os
from include import genereitor
from random import randint
from threading import Thread
import random
pygame.init()
pygame.mixer.init()

def PlayMusic(music):
    dir = os.path.join('music', music)
    pygame.mixer.music.load(dir)
    pygame.mixer.music.play(-1)
    

Moviment = True
TELA_X= 740
TELA_Y = 1500
FontSize= 70
COIN_MOVE = 60
MovObj = 65
MovObj2 = 65
MovObj3 = 65
colisao_x = 0
colisao_y = 2500
X = 740
Y = 1500
power_x = 320
power_y = 1300 
Pulo = False
power_time = 5
point_game = None
try:
    COIN_POINT = int(genereitor.ReadCoins())
except:
    COIN_POINT = 0
COIN_X = randint(50, 500)
COIN_Y = 0
COIN_Y -= randint(800,1500)
mouse_x, mouse_y = 400, 4000
CX = 4000
CY = 900
POINTER = 0
TIME = 0
CARMAX_X = 400
CARMIN_X = 0
click_time = 0
clicked = False
O1X = CARMIN_X
O1Y =0
O1Y -= randint(2400, 3000)

O2X = CARMAX_X
O2Y= 0
O2Y -=  randint(3600, 6000)

O3X = CARMIN_X
O3Y = 0
O3Y -= randint(6600, 8000)

PLAY = False
play_x = 70
play_y = 690

Click_Loja = False
loja_x = 280
loja_y = 970 


GameReset = False
reset_x = 6000
reset_y = 500

cap_x = -40
cap_y =320

cap2_x = -40
cap2_y = 320

MUDO = False
rmusic_x = 140
rmusic_y = 600


pmusic_x = 360
pmusic_y = 600

click_mudo = 0
clicl_mudo2 = 0
button_x = 4000
button_y = 520


exit_x = 230
exit_y = 1100

tela = pygame.display.set_mode((TELA_X, TELA_Y),pygame.SCALED, pygame.FULLSCREEN)
clock = pygame.time.Clock()

pygame.display.set_caption('Street Racing Word')


street = pygame.image.load('img/pista2.png')

street = pygame.transform.scale(street, (X, Y))

textRecord = pygame.font.SysFont('italic', FontSize)




time = pygame.font.SysFont('italic', FontSize)
text = time.render(': '+str(TIME),True,'yellow')
pos_text = text.get_rect()
pos_text.topleft = (50,90)


time2 = pygame.font.SysFont('italic', 150)
text2 = time2.render('Game Over ',True,'red')
pos_text2 = text2.get_rect()
pos_text2.center = (340,2500)

time3 = pygame.font.SysFont('italic', FontSize)
text3 = time3.render(f': {COIN_POINT}',True,'yellow')
pos_text3 = text3.get_rect()
pos_text3.topleft = (50,145)

text4 = textRecord.render('Novo Record:'+str(TIME),True,'yellow','black')
pos_text4 = text4.get_rect()
pos_text4.topleft = (200,2900)

class Play(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/play1.png'))
        self.sprites.append(pygame.image.load('img/play2.png'))
        self.sprites.append(pygame.image.load('img/play3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image =  pygame.transform.scale(self.image, (200,200))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.x = play_x
        self.y = play_y
        self.rect.topleft = self.x, self.y
        self.play = False
    def Click_Play(self):
        self.play = True
    def Click_Return(self):
        self.play = False
    def update(self):
        if self.play == True:
            self.x = 3000
        if self.play == False:
            self.x = 260  
        self.atual += 1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image =  pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/coin1.png'))
        self.sprites.append(pygame.image.load('img/coin2.png'))
        self.sprites.append(pygame.image.load('img/coin3.png'))
        self.sprites.append(pygame.image.load('img/coin4.png'))
        self.sprites.append(pygame.image.load('img/coin5.png'))
        self.sprites.append(pygame.image.load('img/coin6.png'))
        self.sprites.append(pygame.image.load('img/coin7.png'))
        self.sprites.append(pygame.image.load('img/coin8.png'))
        self.sprites.append(pygame.image.load('img/coin9.png'))
        self.sprites.append(pygame.image.load('img/coin10.png'))
        self.sprites.append(pygame.image.load('img/coin11.png'))
        self.sprites.append(pygame.image.load('img/coin12.png'))
        self.sprites.append(pygame.image.load('img/coin13.png'))
        self.sprites.append(pygame.image.load('img/coin14.png'))
        self.sprites.append(pygame.image.load('img/coin15.png'))
        self.sprites.append(pygame.image.load('img/coin16.png'))
        self.sprites.append(pygame.image.load('img/coin17.png'))
        self.sprites.append(pygame.image.load('img/coin18.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image =  pygame.transform.scale(self.image, (100,100))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.x = CARMAX_X
        self.y = COIN_Y
        self.rect.topleft = self.x, self.y
        self.respaw = False
    def reset(self):
        self.respaw = True
        self.x = randint(100,600)
        self.y -= randint(1500,2000)
        
    def update(self):
        self.atual +=  1
        self.y += COIN_MOVE
        
        if self.y >= 1500:
            self.y -= randint(1500, 2000)
            self.x = randint(100,600)
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image =  pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        
        
class Objeto03(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/objeto03.png'))
        self.image = self.sprites[0]
        self.image =  pygame.transform.scale(self.image, (250,450))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = O3X
        self.y = O3Y
        self.rect.topleft = self.x,O3Y
        
    def update(self):
        self.image =  pygame.transform.scale(self.image, (250,450))
        self.rect = self.image.get_rect()
        if O3Y >= 2900:
            if self.x == CARMAX_X:
                self.x = CARMIN_X 
            else:
                self.x = CARMAX_X
        self.rect.topleft = self.x,O3Y
        
class Objeto02(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/objeto02.png'))
        self.image = self.sprites[0]
        self.image =  pygame.transform.scale(self.image, (300,450))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = O2X
        self.y = O2Y
        self.rect.topleft = self.x, O2Y
        
    def update(self):
        self.image =  pygame.transform.scale(self.image, (300,450))
        self.rect = self.image.get_rect()
        if O2Y >= 1900:
            if self.x == CARMAX_X:
                self.x = CARMIN_X
            else:
                self.x = CARMAX_X
        self.rect.topleft = self.x,O2Y
        
        
class Objeto01(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/objeto01.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image =  pygame.transform.scale(self.image, (300,450))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = O1X
        self.y = O1Y
        self.rect.topleft = self.x, O1Y
      
    def update(self):
        self.atual += 1
        self.image =  pygame.transform.scale(self.image, (300,450))
        self.rect = self.image.get_rect()
        if O1Y >= 1900:
            if self.x == CARMAX_X:
                self.x = CARMIN_X
            else:
                self.x = CARMAX_X
        self.rect.topleft = self.x,O1Y
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites2 = []
        self.sprites.append(pygame.image.load('img/player/player01.png'))
        self.sprites.append(pygame.image.load('img/player/player02.png'))
        self.sprites.append(pygame.image.load('img/player/player03.png'))
        self.sprites.append(pygame.image.load('img/player/wing1.png'))
        self.sprites.append(pygame.image.load('img/player/wing2.png'))
        self.sprites.append(pygame.image.load('img/player/wing3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image =  pygame.transform.scale(self.image, (300,450))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (CX, CY)
        self.moviment = False
        self.Wing = False
        
    def OpenWing(self):
        self.Wing = True
        
            
          
    def ClosedWing(self):
        self.Wing = False
                  
    def move(self):
        self.moviment = True  
        
    def update(self):
        
        if self.Wing == True:
            self.atual = 3
            self.atual = self.atual + 1
            if self.atual >= len(self.sprites):
                self.atual = 5
                
        if self.Wing == False:
            self.atual = self.atual + 1
            if self.atual >= 3:
                self.atual = 0
                
        if self.moviment == True:
            CX, cy = pygame.mouse.get_pos()
            CX -=200
            if CX <= CARMIN_X:
                CX = CARMIN_X
            if CX>= CARMAX_X:
                CX = CARMAX_X
            self.rect.x = CX
        
        self.image = self.sprites[self.atual]
        self.image =  pygame.transform.scale(self.image, (300,450))
             
class Explosao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites =[]
        self.sprites.append(pygame.image.load('img/explosao0.png'))
        self.sprites.append(pygame.image.load('img/explosao1.png'))
        self.sprites.append(pygame.image.load('img/explosao2.png'))
        self.sprites.append(pygame.image.load('img/explosao3.png'))
        self.sprites.append(pygame.image.load('img/explosao4.png'))
        self.sprites.append(pygame.image.load('img/explosao5.png'))
        self.sprites.append(pygame.image.load('img/explosao6.png'))
        self.sprites.append(pygame.image.load('img/explosao7.png'))
        self.sprites.append(pygame.image.load('img/explosao8.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (300,300))
        self.rect = self.image.get_rect()
        self.x= colisao_x
        self.y = colisao_y
        self.rect.topleft = (self.x, self.y)
    
            
    def update(self):
        self.x = colisao_x
        self.y = colisao_y
        self.rect.topleft = self.x, self.y
        self.atual =  self.atual + 1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (300,300))
        
class Power(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/player/power.png'))
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.x = power_x
        self.y = power_y
        self.rect.topleft =self.x, self.y
        
    def update(self):
        if clicked:
            power_x = 4000
        if clicked == False:
            power_x = 320
        self.image = pygame.transform.scale(self.image, (100,100))
        self.x = power_x
        self.y = power_y
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y
        
        
        
     

class Reset(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/reset1.png'))
        self.sprites.append(pygame.image.load('img/reset2.png'))
        self.sprites.append(pygame.image.load('img/reset3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.x = reset_x
        self.y = reset_y
        self.rect.topleft =self.x, self.y
        self.on = False
    def On(self):
        self.on = True
    def update(self):
        self.atual += 1
        if self.on == True:
            self.x = reset_x
        if self.on == False:
            self.x = reset_x
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image =  pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        
        
class Pista(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/pista1.png'))
        self.sprites.append(pygame.image.load('img/pista2.png'))
        self.sprites.append(pygame.image.load('img/pista3.png'))
        self.sprites.append(pygame.image.load('img/pista4.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (X,Y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
    def update(self):
        self.atual +=1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (X,Y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        
class Loja(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/loja1.png'))
        self.sprites.append(pygame.image.load('img/loja2.png'))
        self.sprites.append(pygame.image.load('img/loja3.png'))
        self.sprites.append(pygame.image.load('img/loja4.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.rect.topleft = (loja_x,loja_y)
    def update(self):
        self.atual += 1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.rect.topleft = (loja_x,loja_y)
        
class CapMain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/index.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(800, 1200))
        self.rect = self.image.get_rect()
        self.rect.topleft = (cap_x, cap_y)
        
    def update(self):
        self.atual += 1 
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(800, 1200))
        self.rect = self.image.get_rect()
        self.rect.topleft = (cap_x, cap_y)
        
class Settings(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/bg.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (800, 1200))
        self.rect = self.image.get_rect()
        self.rect.topleft = (cap2_x, cap2_y)
    def update(self):
        self.atual += 1 
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (800, 1200))
        self.rect = self.image.get_rect()
        self.rect.topleft = (cap2_x, cap2_y)
        
class ButtonPlayMusic(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/offmusic.png'))
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (200,150))
        self.x, self.y = pmusic_x, pmusic_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        
    def update(self):
        if Click_Loja == True:
            self.x = 360
        if Click_Loja == False:
            self.x = 4000
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (200,150))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        
class Button_Return(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/return.png'))
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.topleft = (button_x, button_y)
    def update(self):
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (button_x, button_y)
        
        
class ExitGame(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/exit.png'))
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (250, 150))
        self.x, self.y = exit_x, exit_y
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        
    def update(self):
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (250, 150))
        self.x, self.y = exit_x, exit_y
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        

class RemoveMusic(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/onmusic.png'))
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.x, self.y = rmusic_x, rmusic_y
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
    def RemoveScreen(self):
        self.x = 4000
    def update(self):
        if PLAY:
            self.x = 4000
        if Click_Loja == True:
            self.x60
        if Click_Loja == False:
            self.x = 4000
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (200, 150))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        
        
class ShowCoins(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/coin1.png'))
        self.sprites.append(pygame.image.load('img/coin2.png'))
        self.sprites.append(pygame.image.load('img/coin3.png'))
        self.sprites.append(pygame.image.load('img/coin4.png'))
        self.sprites.append(pygame.image.load('img/coin5.png'))
        self.sprites.append(pygame.image.load('img/coin6.png'))
        self.sprites.append(pygame.image.load('img/coin7.png'))
        self.sprites.append(pygame.image.load('img/coin8.png'))
        self.sprites.append(pygame.image.load('img/coin9.png'))
        self.sprites.append(pygame.image.load('img/coin10.png'))
        self.sprites.append(pygame.image.load('img/coin11.png'))
        self.sprites.append(pygame.image.load('img/coin12.png'))
        self.sprites.append(pygame.image.load('img/coin13.png'))
        self.sprites.append(pygame.image.load('img/coin14.png'))
        self.sprites.append(pygame.image.load('img/coin15.png'))
        self.sprites.append(pygame.image.load('img/coin16.png'))
        self.sprites.append(pygame.image.load('img/coin17.png'))
        self.sprites.append(pygame.image.load('img/coin18.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (1,140)
    def update(self):
        self.atual += 1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (1,140)
        
class Point(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/point1.png'))
        self.sprites.append(pygame.image.load('img/point2.png'))
        self.sprites.append(pygame.image.load('img/point3.png'))
        self.sprites.append(pygame.image.load('img/point4.png'))
        self.sprites.append(pygame.image.load('img/point5.png'))
        self.sprites.append(pygame.image.load('img/point6.png'))
        self.sprites.append(pygame.image.load('img/point7.png'))
        self.sprites.append(pygame.image.load('img/point8.png'))
        self.sprites.append(pygame.image.load('img/point9.png'))
        self.sprites.append(pygame.image.load('img/point10.png'))
        self.sprites.append(pygame.image.load('img/point11.png'))
        self.sprites.append(pygame.image.load('img/point12.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (120,120))
        self.rect = self.image.get_rect()
        self.rect.topleft = (-30,50)
    def update(self):
        self.atual += 1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(120,120))
        self.rect = self.image.get_rect()
        self.rect.topleft = (-30,50) 
        
        
SHOW_POINT = Point()
COINS = ShowCoins()
EXIT = ExitGame()      
BUTTON_RETURN = Button_Return()
buttonplaymusic = ButtonPlayMusic()
remove_music = RemoveMusic()      
settings = Settings()    
CAPA = CapMain()
loja = Loja()
pista = Pista()        
play = Play()
RESET = Reset()
POWER = Power()
COIN = Coins()
OBJ = Objeto01()
OBJ2 = Objeto02()
OBJ3 = Objeto03()
player = Player()
colisao = Explosao()
SHOWPOINT = pygame.sprite.Group()
SHOWCOINS = pygame.sprite.Group()
EXITGAME = pygame.sprite.Group()
BUTTONRETURN = pygame.sprite.Group()
BUTTON_MUSIC = pygame.sprite.Group()
REMOVE_MUSIC = pygame.sprite.Group()
SETTINGS = pygame.sprite.Group()
CAPAMAIN = pygame.sprite.Group()
LOJA = pygame.sprite.Group()
CLOJA01 = pygame.sprite.Group()
PISTA = pygame.sprite.Group()
Play = pygame.sprite.Group()
RESETS = pygame.sprite.Group()
SPRITES = pygame.sprite.Group()
CARROPLAYER = pygame.sprite.Group()
OBJETO01 = pygame.sprite.Group()
EFECT = pygame.sprite.Group()
CASH = pygame.sprite.Group()
SHOWPOINT.add(SHOW_POINT)
EXITGAME.add(EXIT)
SHOWCOINS.add(COINS)
BUTTONRETURN.add(BUTTON_RETURN)
SETTINGS.add(settings)
REMOVE_MUSIC.add(remove_music)
BUTTON_MUSIC.add(buttonplaymusic)
CAPAMAIN.add(CAPA)
LOJA.add(loja)
PISTA.add(pista)
EFECT.add(POWER)
CASH.add(COIN)
OBJETO01.add(OBJ)
OBJETO01.add(OBJ2)
OBJETO01.add(OBJ3)
CARROPLAYER.add(player)
SPRITES.add(colisao)
Play.add(play)
RESETS.add(RESET)
#MUSICA DO JOGO
pygame.mixer.music.load('music/music.mp3')
# Reproduzir a músicas
PlayMusic('music.mp3')
gameover = pygame.mixer.Sound('music/colisao.mp3')
Motor_Sond = pygame.mixer.Sound('music/motor.mp3')
SondCoin = pygame.mixer.Sound('music/coin.mp3')

clicked = False
click_time = 0  # Inicialize click_time com 0 fora do loop principal

# ...
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if POWER.rect.collidepoint(event.pos):
                click_time = pygame.time.get_ticks()
                clicked = True


    PISTA.draw(tela)
    PISTA.update()
    # Desenhe a sprite
    #screen.blit(sprite_image, sprite_rect)
    #mostrar na tela o objeto 01    e 02
    OBJETO01.draw(tela)
    OBJETO01.update()
    #mostrar moedas na tela
    CASH.draw(tela)
    CASH.update()
    #Mostrar carro do player na tela
    CARROPLAYER.draw(tela)
    CARROPLAYER.update()
    #Mostrar explosao no momento da colisao
    SPRITES.draw(tela)
    SPRITES.update()
    #mostrar placa de tempo na tela
    EFECT.draw(tela)
    EFECT.update()
    tela.blit(text4, pos_text4)
    tela.blit(text, pos_text)
    tela.blit(text2, pos_text2)
    tela.blit(text3, pos_text3)
    RESETS.draw(tela)
    RESETS.update()
    SETTINGS.draw(tela)
    SETTINGS.update()
    BUTTONRETURN.draw(tela)
    BUTTONRETURN.update()
    BUTTON_MUSIC.draw(tela)
    BUTTON_MUSIC.update()
    REMOVE_MUSIC.draw(tela)
    REMOVE_MUSIC.update()
    CAPAMAIN.draw(tela)
    CAPAMAIN.update()
    LOJA.draw(tela)
    LOJA.update()
    Play.draw(tela)
    Play.update()
    EXITGAME.draw(tela)
    EXITGAME.update()
    SHOWCOINS.draw(tela)
    SHOWCOINS.update()
    SHOWPOINT.draw(tela)
    SHOWPOINT.update()
    
    
    #Movimento do objeto 01
    COIN_Y+= MovObj
    O3Y += MovObj
    O2Y += MovObj
    O1Y += MovObj
    if clicked:
        Pulo = True
        current_time_ms = pygame.time.get_ticks()
        elapsed_seconds = (current_time_ms - click_time) // 1000
    
        
        player.OpenWing()
        if int(elapsed_seconds) >= 5:
            player.ClosedWing()
            power_x = 4000
            Pulo =False
    
        if int(elapsed_seconds) >= 10:
            power_x = 320
            clicked = False
    

    if PLAY == False or GameReset == False:
        MovObj = 0
        MovObj2 = 0
        MovObj3 = 0
        Moviment =False
        COIN_MOVE = 0
        power_x = 4000
        POINTER = 21
    if PLAY == True or GameReset == True:
        MovObj = 100
        MovObj2 = 100
        MovObj3 = 100
        Moviment =True
        COIN_MOVE = 50
        POINTER = 0
        power_x = 320
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
    player.move()
    #configurar touch
    mouse_x -= 200
    CARROPLAYER.topleft = mouse_x, mouse_y
    mouse_pos = pygame.mouse.get_pos()
    
    #Movimento de Objetos
    if COIN_Y >= 1500:
        COIN_Y -= randint(800,1000)
        COIN_X = randint(50,400)
        
    if O1Y >= 2000:     
        
        O1Y -= randint(2600, 3000)
            
            
    if O2Y >= 2000:
        
        O2Y -=  randint(4600, 6000)
            
    if O3Y >=2000:
        
        
        O3Y -= randint(7600,8000)
     
    elif POINTER < 20:
        POINTER = POINTER +1 
        TIME = TIME +1
        time = pygame.font.SysFont('italic', FontSize)
        text = time.render(': '+str(TIME),True,'yellow')
        pos_text = text.get_rect()
        pos_text.topleft = (50,90)
   
    get_money = pygame.sprite.spritecollide(player,CASH, False, pygame.sprite.collide_mask)
    if get_money != []:
        SondCoin.play()
        COIN_POINT += randint(1,100)
        text3 = time3.render(f': {COIN_POINT}',True,'yellow')
        pos_text3 = text3.get_rect()
        pos_text3.topleft = (50,145)
        COIN.reset()
        con_string = str(COIN_POINT)
        genereitor.SaveCoins(con_string)
        
        
    mouse_pos = pygame.mouse.get_pos()
    
    click_exit = [sprite for sprite in EXITGAME if sprite.rect.collidepoint(mouse_pos)]
    for sprite in click_exit:
          loop = False
          
    mouse_pos = pygame.mouse.get_pos()
    
    click_mude = [sprite for sprite in REMOVE_MUSIC if sprite.rect.collidepoint(mouse_pos)]
    for sprites in click_mude:
        if MUDO == True:
            PlayMusic('music.mp3')
            MUDO = False
    mouse_pos = pygame.mouse.get_pos()
    
    click_return = [sprite for sprite in BUTTONRETURN if sprite.rect.collidepoint(mouse_pos)]
    for sprite in click_return:
        play.Click_Return()
        pmusic_x= 4000
        cap2_x=4000
        rmusic_x = 4000
        cap_x = -40
        loja_x = 280
        button_x = 4000
        exit_x = 230
    mouse_pos = pygame.mouse.get_pos()
    
    click_music = [sprite for sprite in BUTTON_MUSIC if sprite.rect.collidepoint(mouse_pos)]
    for sprites in click_music:
        if MUDO == False:
            pygame.mixer.music.stop()
            
            MUDO = True
    mouse_pos = pygame.mouse.get_pos()
    
    click_power = [sprite for sprite in Play if sprite.rect.collidepoint(mouse_pos)]
    for sprite in click_power:
        play.Click_Play()
        Click_Loja  = False
        PLAY=True
        rmusic_x = 4000
        pmusic_x = 4000
        exit_x = 4000
        loja_x = 2000
        cap_x =4000
        cap2_x = 4000
        
    mouse_pos = pygame.mouse.get_pos()
    click_loja = [sprite for sprite in LOJA if sprite.rect.collidepoint(mouse_pos)]
    for sprite in click_loja:
        play.Click_Play()
        loja_x = 2000
        power_x = 4000
        cap_x = 4000
        cap2_x = -40
        pmusic_x = 240
        rmusic_x = 360
        button_x= 450
        exit_x = 4000
        Click_Loja = True
        
    mouse_pos = pygame.mouse.get_pos()
    click_power = [sprite for sprite in RESETS if sprite.rect.collidepoint(mouse_pos)]
    for sprite in click_power:
        if GameReset == True:
            allcoin = int(genereitor.ReadCoins())
            if allcoin <= 1000:
                PLAY= False
                GameReset =False
               # text3.rect.center = ()
                COIN_MOVE = 0
                colisao_y = 3000
                pos_text4.topleft= (200, 1900)
                pos_text2.center = (0, 4000)
                reset_x = 6000
                Moviment = False
                MovObj = 0
                MovObj2 = 0
                MovObj3 = 0
                O1Y -= randint(3400,4000)
                O2Y -=  randint(4800, 60000)
                O3Y -= randint(6800, 8000)
                COIN_Y -= randint(800,1500)
                TIME = 0
                POINT = 2100
                exit_x = 230
                cap_x= -40
                loja_x=280
                play.Click_Return()
                
            else:
                allcoin -= 1000
                genereitor.SaveCoins(str(allcoin))
                COIN_POINT = allcoin
                text3 = time3.render(f': {COIN_POINT}',True,'yellow')
                pos_text3 = text3.get_rect()
                pos_text3.topleft = (50,145)
                GameReset = False
                reset_x = 6000
                MovObj = 60
                MovObj2 = 60
                MovObj3 = 60
                O1Y -= randint(3400,4000)
                O2Y -=  randint(4800, 60000)
                O3Y -= randint(6800, 8000)
                COIN_Y -= randint(800,1500)
                #if MUDO ==False:
                    #pygame.mixer.music.play(-1)
                Moviment =True
                COIN_MOVE = 50
                colisao_y = 3000
                pos_text4.topleft= (200, 1900)
                pos_text2.center = (0, 4000)
                
                power_x = 320
                RESET.On()
        else:
            PLAY = True
            GameReset = True
    
          

    colisao = pygame.sprite.spritecollide(player, OBJETO01, False, pygame.sprite.collide_mask)
    if colisao != []:
        if Pulo == True:
            #player.OpenWing()
            pass
        else:
            MovObj = 0
            MovObj2 = 0
            MovObj3 = 0
            
            Moviment =False
            colisao_x=mouse_x
            colisao_y =CY
            POINTER= 21
            point_game = genereitor.SaveRecords(int(TIME))
            if point_game == 'Novo Record':
                text4 = textRecord.render('New Record:'+str(TIME),True,'red')
                pos_text4.topleft = (200,1000)
                point_game = None
            gameover.play()
            pos_text2.topleft = (80, 800)
            COIN_MOVE = 0
            power_x = 4000
            reset_x = 270
            PLAY=False
            
    pygame.display.flip()
    clock.tick(60)

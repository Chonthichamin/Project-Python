import pygame
import time
import random
pygame.init()
catbang = pygame.display.set_mode((900,350))
pygame.display.set_caption('CATBANG')
clock = pygame.time.Clock()


start = [pygame.image.load('spacew.png'),pygame.image.load('spaceb.png')]
cat = [pygame.image.load('cw.png'),pygame.image.load('cat_walk-2.png'),pygame.image.load('cat_walk-4.png'),pygame.image.load('cat_walk-6.png')]
mim = [pygame.image.load('mim1-0.png'),pygame.image.load('mim1-2.png'),pygame.image.load('mim1-4.png')]                                                      
mik = [pygame.image.load('mim2-0.png'),pygame.image.load('mim2-2.png'),pygame.image.load('mim2-4.png')]                 
mio = [pygame.image.load('mim3-1.png'),pygame.image.load('mim3-2.png'),pygame.image.load('mim3-3.png')]
mij = [pygame.image.load('mim4-1.png'),pygame.image.load('mim4-2.png'),pygame.image.load('mim4-3.png')]
son = pygame.image.load('soon.png')
heart = [pygame.image.load('heart1.png'),pygame.image.load('heart2.png'),pygame.image.load('heart3.png'),pygame.image.load('bheart.png')]
back = [pygame.image.load('1nback.png'),pygame.image.load('2nback.png'),pygame.image.load('4nback.png'),pygame.image.load('3nback.png')]
back_move = [pygame.image.load('mback.png'),pygame.image.load('nback.png'),pygame.image.load('gback.png')]
stop = [pygame.image.load('over.png'),pygame.image.load('overw.png')]
sound = pygame.mixer.music.load('soundd.mp3')
pbullet = pygame.mixer.Sound('bult.wav')
phit = pygame.mixer.Sound('hood.wav')
pchon = pygame.mixer.Sound('HAMPOST.wav')

global lv
class mon(object):
    i = 0
    def __init__(self,c):
        self.point = 2
        self.c = c
        if self.c == 1 or self.c== 2:
         self.y = 95
        if self.c == 3:
            self.y = 75
        if self.c == 4:
            self.y = 140
        self.x = random.randint(900,1000)
    def move(self):
        if(lv == 1):
            self.x -= 2
        elif (lv == 2):
            self.x -= 4
        elif (lv == 3):
            self.x -= 5
        else:
            self.x -= 8
            
        if(self.x < -100):
            self.x = 950
        if(self.c == 1):
            catbang.blit(mim[(i//20)%3],(self.x,self.y))
        elif(self.c == 2):
            catbang.blit(mik[(i//20)%3],(self.x,self.y))
        elif(self.c == 3):
            catbang.blit(mio[(i//20)%3],(self.x,self.y))
        else:
            catbang.blit(mij[(i//20)%3],(self.x,self.y))

class bull(object):
    def __init__(self,x):
        self.x = x
        self.y = 160
    def move(self):
        self.x += 2
        catbang.blit(son,(self.x,self.y))

inputkey = True
game_end = True
        
while(game_end):
    pygame.mixer.music.play(-1)
    game = False
    lv = 1
    i = 0
    stage = 0
    monnum = 0
    x_cat = -80
    x_move = 0
    x_eiei = 0
    monlist = []
    mon2 = []
    sonlist=[]
    son2=[]
    g = 0
    power = 3
    screen = 0
    bback = 0
    
    while not game:
        i+=1
        g+=1
        screen += 1
        
        if(i == 1000):
            i = 0
        if(screen == 50):
            screen = 0
            
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE] and inputkey:          
            if stage == 0 :
                 stage=1
                 g = 0
            if stage == 1 and g > 50 and x_cat == 100:
                g = 0
                sonlist.append(bull(x_cat+90))
                pbullet.play()
                
            if(stage ==    2):
                break
            inputkey = False           
            
        if(not keys[pygame.K_SPACE]) :
            inputkey = True
                 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = True
                game_end = False
                
        if(stage == 0):
            catbang.blit(back[0],(0,0))
            if(screen <30):
                catbang.blit(start[0],(200,155))
            else:
                catbang.blit(start[1],(200,150))
                
        elif(stage == 1):
            bback += 1
            if (bback < 1500):
                catbang.blit(back[0],(x_move,0))
                catbang.blit(back_move[0],(x_eiei,0))
                
            elif (1500 < bback < 3500):
                if (1501 == bback ):
                    x_move = 0
                    lv = 2
                    x_eiei = 0
                catbang.blit(back[1],(x_move,0))
                catbang.blit(back_move[1],(x_eiei,0))
                
            elif (3500 < bback < 6000):
                if (3501 == bback ):
                    x_move = 0
                    lv = 3
                    x_eiei = 0
                catbang.blit(back[2],(x_move,0))
                catbang.blit(back_move[2],(x_eiei,0))
                
            else:
                if (6001 == bback ):
                    x_move = 0
                    lv = 4
                    x_eiei = 0
                catbang.blit(back[3],(x_move,0))
                catbang.blit(back_move[2],(x_eiei,0))
                
            if power == 3:
                catbang.blit(heart[2],(0,0))
            elif power == 2:
                catbang.blit(heart[1],(0,0))
            elif power == 1:
                catbang.blit(heart[0],(0,0))

            catbang.blit(cat[(i//10)%4],(x_cat,90))
            
            if(x_cat <100):
                x_cat+=1
            else:
                x_move -= 1
                x_eiei -= 0.8
                
            if(lv == 1):
                if(i % 100 == 0):
                    monlist.append(mon(random.choice([1,2,3,4])))
            elif lv == 2:
                if(i % 80 == 0):
                    monlist.append(mon(random.choice([1,2,3,4])))
            elif lv == 3:
                if(i % 60 == 0):
                    monlist.append(mon(random.choice([1,2,3,4])))      
            else:
                if(i % 40 == 0):
                    monlist.append(mon(random.choice([1,2,3,4])))
            mon2 = monlist
            
        for mon1 in monlist:
            mon1.move()
        son2 = sonlist
        for son1 in sonlist:
            son1.move()
            
        for mone in mon2:
            if(mone.x  - (x_cat + 40) < 0):
                monlist.remove(mone)
                power -= 1
                pchon.play()

        mon2 = monlist
        son2 = sonlist
        
        for bul in son2:
            for mone in monlist:
                if (mone.x - (bul.x+40)<-70):
                    monlist.remove(mon2[0])
                    sonlist.remove(bul)
                    phit.play()
                    
        mon2 = monlist
        son2 = sonlist
        
        for bul in son2:
            if(bul.x > 600):
                sonlist.remove(bul)
                
        mon2 = monlist
        son2 = sonlist
            
        if(stage == 2):
            catbang.blit(heart[3],(0,0))
            if(screen <30):
                catbang.blit(stop[0],(200,155))
            else:
                catbang.blit(stop[1],(200,150))
                
        if(power <= 0):
            stage = 2
            monlist.clear()
            mon2.clear()
            sonlist.clear()
            son2.clear()
        
        pygame.display.update()
        clock.tick(100)
    
   
pygame.quit()


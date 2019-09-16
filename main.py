import pygame
import under
import time
from pygame.locals import *
screen = pygame.display.set_mode((1280,720),HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption('Saper zbigniewa')

wymiary=[int(1280/(under.rozmiar[1]+1.25)),int((1280/(under.rozmiar[1]+1.25))/16*10),int(1280/(under.rozmiar[1]+1.25)/4)]


p0 = pygame.image.load("open0.gif").convert()
p1 = pygame.image.load("open1.gif").convert()
p2 = pygame.image.load("open2.gif").convert()
p3 = pygame.image.load("open3.gif").convert()
p4 = pygame.image.load("open4.gif").convert()
p5 = pygame.image.load("open5.gif").convert()

p6 = pygame.image.load("open6.gif").convert()
p7 = pygame.image.load("open7.gif").convert()
p8 = pygame.image.load("open8.gif").convert()
p10 = pygame.image.load("bomba.gif").convert()
p11 = pygame.image.load("blank.gif").convert()
p12 = pygame.image.load("flaga.gif").convert()
p13 = pygame.image.load("kutas.jpg").convert()
kafelki=[p0,p1,p2,p3,p4,p5,p6,p7,p8,p10,p10,p11,p12]



borderbok = pygame.image.load("borderdul.gif").convert()
borderdul = pygame.image.load("borderbok.gif").convert()
bordertl = pygame.image.load("bordertl.gif").convert()
bordertr = pygame.image.load("bordertr.gif").convert()
borderbl = pygame.image.load("borderbl.gif").convert()
borderbr = pygame.image.load("borderbr.gif").convert()


borderbok =pygame.transform.scale(borderbok, (wymiary[1],wymiary[1]))
borderdul =pygame.transform.scale(borderdul, (wymiary[1],wymiary[1]))
bordertl =pygame.transform.scale(bordertl, (wymiary[1],wymiary[1]))
bordertr =pygame.transform.scale(bordertr, (wymiary[1],wymiary[1]))
borderbl=pygame.transform.scale(borderbl, (wymiary[1],wymiary[1]))
borderbr    =pygame.transform.scale(borderbr, (wymiary[1],wymiary[1]))


gra=True



for i in range(len(kafelki)):
    kafelki[i] = pygame.transform.scale(kafelki[i], (wymiary[0],wymiary[0]))


def odslonn(x,y):

    polee=under.stan[x][y]
    polee[1]=True
    screen.blit(kafelki[polee[0]],(wymiary[1]+int(wymiary[0])*y,wymiary[1]+int(wymiary[0])*x))


def game_over():
    global gra
    gra = False
    screen.fill((0,0,0))
    pygame.display.update()
    time.sleep(1)
    screen.fill((0,0,0))
    pygame.display.update()
    voltar = pygame.Rect(0, 0, 2000, 1500)

    pygame.display.update()
    pygame.draw.rect(screen, [255,0,0], voltar)
    pygame.draw.rect(screen, [255,0,0], voltar)
    pygame.display.flip()
    screen.blit(p13,(400,200))
    pygame.display.flip()

    time.sleep(5)
    
    under.miner()
    print("\n\n\n\n")
    under.geolog()
    load_border()
    gra=True
    load_pole()
    klik=False
    




def load_border():
    global wymiary
    rozmiar=under.rozmiar

    for i in range(rozmiar[0]):
        screen.blit(borderbok, (0,i*wymiary[0]+wymiary[1]))
        screen.blit(borderbok, (0,i*wymiary[0]+wymiary[1]+wymiary[2]))
        screen.blit(borderbok, (0,i*wymiary[0]+wymiary[1]+wymiary[2]*2))
        screen.blit(borderbok, (0,i*wymiary[0]+wymiary[1]+wymiary[2]*3))

        screen.blit(borderbok, (rozmiar[1]*wymiary[0]+wymiary[1],i*wymiary[0]+wymiary[1]))
        screen.blit(borderbok, (rozmiar[1]*wymiary[0]+wymiary[1],i*wymiary[0]+wymiary[1]+wymiary[2]))
        screen.blit(borderbok, (rozmiar[1]*wymiary[0]+wymiary[1],i*wymiary[0]+wymiary[1]+wymiary[2]*2))
        screen.blit(borderbok, (rozmiar[1]*wymiary[0]+wymiary[1],i*wymiary[0]+wymiary[1]+wymiary[2]*3))

        
    for i in range(rozmiar[1]):
        screen.blit(borderdul, (i*wymiary[0]+wymiary[1],0))
        screen.blit(borderdul, (i*wymiary[0]+wymiary[1]+wymiary[2],0))
        screen.blit(borderdul, (i*wymiary[0]+wymiary[1]+wymiary[2]*2,0))
        screen.blit(borderdul, (i*wymiary[0]+wymiary[1]+wymiary[2]*3,0))

        screen.blit(borderdul, (i*wymiary[0]+wymiary[1],rozmiar[0]*wymiary[0]+wymiary[1]))
        screen.blit(borderdul, (i*wymiary[0]+wymiary[1]+wymiary[2]*1,rozmiar[0]*wymiary[0]+wymiary[1]))
        screen.blit(borderdul, (i*wymiary[0]+wymiary[1]+wymiary[2]*2,rozmiar[0]*wymiary[0]+wymiary[1]))
        screen.blit(borderdul, (i*wymiary[0]+wymiary[1]+wymiary[2]*3,rozmiar[0]*wymiary[0]+wymiary[1]))


    screen.blit(bordertl, (0,0))
    screen.blit(bordertr, (rozmiar[1]*wymiary[0]+wymiary[1],0))
    screen.blit(borderbl, (0,rozmiar[0]*wymiary[0]+wymiary[1]))
    screen.blit(borderbr, (rozmiar[1]*wymiary[0]+wymiary[1],rozmiar[0]*wymiary[0]+wymiary[1]))  

        
    pygame.display.flip()

def puste(x,y):
    odslonn(x,y)
    pole=under.stan 
    rozmiar=under.rozmiar  
    print([x,y])
    
    if x > 0:
        
        if pole[x-1][y][0]==0 and pole[x-1][y][1]== False:puste(x-1,y)
        else: odslonn(x-1,y) 
        
        if y > 0:
            if pole[x-1][y-1][0]==0 and pole[x-1][y-1][1]==False:puste(x-1,y-1)
            else: odslonn(x-1,y-1) 
        if y <(under.rozmiar[1]-1):
            if pole[x-1][y+1][0]==0 and pole[x-1][y+1][1]==False:puste(x-1,y+1)
            else: odslonn(x-1,y+1)
    if x < (rozmiar[0]-1):
        
        if pole[x+1][y][0]==0 and pole[x+1][y][1]==False:puste(x+1,y)
        else: odslonn(x+1,y)

        if y > 0:
            if pole[x+1][y-1][0]==0 and pole[x+1][y-1][1]==False:puste(x+1,y-1)
            else: odslonn(x+1,y-1)
        if y <(rozmiar[1]-1):
            if pole[x+1][y+1][0]==0 and pole[x+1][y+1][1]==False:puste(x+1,y+1)
            else: odslonn(x+1,y+1)

    
    
    if y > 0:
            if pole[x][y-1][0]==0 and pole[x][y-1][1]==False:puste(x,y-1)
            else: odslonn(x,y-1)
    if y <(rozmiar[1]-1):
            if pole[x][y+1][0]==0 and pole[x][y+1][1]==False:puste(x,y+1)
            else: odslonn(x,y+1)

    









def load_pole():
    global wymiary
    global kafelki
    stan=under.stan
    rzadnr=0
    if gra:
        for rzad in stan:
            polenr=0
            for pole in rzad:
                if gra:
                    if pole[1]:
                        if pole[0]==0:
                            
                            puste(rzadnr,polenr)
                        elif pole[0]==10:
                            screen.fill((0,0,0))
                            pygame.display.update()
                            game_over()
                            
                            
                        else:
                            screen.blit(kafelki[pole[0]],(wymiary[1]+wymiary[0]*polenr,wymiary[1]+wymiary[0]*rzadnr))
                    else:
                        if pole[2]==1:
                            screen.blit(kafelki[12],(wymiary[1]+wymiary[0]*polenr,wymiary[1]+wymiary[0]*rzadnr))
                        else:
                            screen.blit(kafelki[11],(wymiary[1]+wymiary[0]*polenr,wymiary[1]+wymiary[0]*rzadnr))
                    polenr+=1
            rzadnr+=1
        pygame.display.flip()
    
def odslon(y,x):
    #screen.blit(kafelki[11],(wymiary[0]*x+wymiary[1],int(wymiary[0])*y+wymiary[1]))
    if min([x,y])>=0:
        if under.stan[y][x][2]==0:
            under.stan[y][x][1]=True
            load_pole()
def flaga(y,x):
    
    pole=under.stan[y][x]
    print(pole)
    if pole[1]==False:
        
        if pole[2]==1:
            screen.blit(kafelki[11],(wymiary[0]*x+wymiary[1],int(wymiary[0])*y+wymiary[1]))
            pole[2]=0
        else:
            print("beniz")
            screen.blit(kafelki[12],(wymiary[0]*x+wymiary[1],int(wymiary[0])*y+wymiary[1]))
            
            pole[2]=1
    pygame.display.flip()    


load_border()
load_pole()


klik=False
pygame.time.Clock()



running = True
while (running): # loop listening for end of game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            czasdown=pygame.time.get_ticks()
            klik=True

            print((pos[0]-wymiary[1])//(wymiary[0]))
            
        if event.type == MOUSEBUTTONUP :
            czasup=pygame.time.get_ticks()
            klikczas=czasup-czasdown
            print("dupa")
            if klik:
                if gra:
                    if klikczas > 300:
                        flaga(((pos[1]-wymiary[1])//(wymiary[0])),((pos[0]-wymiary[1])//(wymiary[0])))
                    else:
                        odslon(((pos[1]-wymiary[1])//(wymiary[0])),((pos[0]-wymiary[1])//(wymiary[0])))
                


#loop over, quite pygame
pygame.quit()
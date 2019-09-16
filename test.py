import pygame
from pygame.locals import *
screen = pygame.display.set_mode((1280,720),HWSURFACE|DOUBLEBUF|RESIZABLE)
running = True
klik=False
pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN :
            print("siusiak")
            czasdown=pygame.time.get_ticks()
            klik=True
            
            

        if event.type == MOUSEBUTTONUP :
            czasup=pygame.time.get_ticks()
            print("dupa")
            if klik:
                print(czasdown,czasup)
                print(czasup-czasdown)
            
pygame.quit()

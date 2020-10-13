import pygame
from  random import *
CZERWONY =(255,0,0)
ROZMIAR_OKNA = (800,600)
pygame.init()
pygame.display.set_caption('Projekt osadzanie')
okno = pygame.display.set_mode(ROZMIAR_OKNA)
def kryształek():
    x = randint(1,ROZMIAR_OKNA[0]-2)
    y = 1
    while True:
        translate = randint(-1,1)
        if 1 < x + translate <ROZMIAR_OKNA[0]-1:
            x = x + translate
            y =y + 1
        if okno.get_at((x,y+1)) == CZERWONY or okno.get_at((x+1,y+1)) == CZERWONY or okno.get_at((x-1,y+1)) == CZERWONY:
            return (x,y)
pygame.draw.rect(okno,CZERWONY,(0,ROZMIAR_OKNA[1]-10,ROZMIAR_OKNA[0],10))
while True:
    #okno.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.draw.circle(okno,CZERWONY,kryształek(),0)   
    
    pygame.display.flip()   #odświeżenie ekranu
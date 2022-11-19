import sys
import pygame
from variables import (pantalla,fuente,Español, Ingles)
import variables 

pygame.display.set_caption('data/imagenes/icono.PNG')
icon = pygame.image.load('data/imagenes/icono.PNG').convert_alpha()
pygame.display.set_icon (icon)
pygame.display.set_caption('Game Over')

pygame.display.set_caption('Monkey Guard')
fondo = pygame.image.load('data/imagenes/Background.jpeg').convert_alpha()
# game loop
run = True
while run:

    pantalla.blit(fondo, [0, 0])

    if not variables.botonM.draw(pantalla):
        pass
    else:
        exec(open('./Niveles.py', encoding="utf-8").read())
        sys.exit()
    if variables.botonR.draw(pantalla):
        sys.exit()
    if variables.ingles ==True:
        pantalla.blit(fuente.render(Ingles[0],1,(0,0,0)), (242, 365))
        pantalla.blit(fuente.render(Ingles[1],1,(0,0,0)), (245, 465))
    else:
        pantalla.blit(fuente.render(Español[0],1,(0,0,0)), (220, 365))
        pantalla.blit(fuente.render(Español[1],1,(0,0,0)), (232, 465))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()

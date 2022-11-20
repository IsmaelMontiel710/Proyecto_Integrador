import sys
import pygame
import button
import variables
from variables import (pantalla, botonMorado)
# create display window

pygame.display.set_caption('data/imagenes/icono.PNG')
icon = pygame.image.load('data/imagenes/icono.PNG').convert_alpha()
pygame.display.set_icon (icon)

pygame.display.set_caption('Game Over')
fondo = pygame.image.load('data/imagenes/Game_over_español.png').convert_alpha()
# load button images
retornar = pygame.image.load(botonMorado).convert_alpha()


# create button instances
ret_button = button.Button(360, 400, retornar, 1.1)

# game loop
run = True
while run:

    pantalla.blit(fondo, [0, 0])

    if not ret_button.draw(pantalla):
        pass
    else:
        exec(open('./Niveles.py', encoding="utf-8").read())
        sys.exit()
    if variables.ingles==True:
        pantalla.blit(variables.fuente.render(variables.Ingles[2],1,(0,0,0)), (370, 445))
    else:
        pantalla.blit(variables.fuente.render(variables.Español[2],1,(0,0,0)), (370, 445))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

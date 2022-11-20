import sys
import pygame
import button
import variables
from variables import (W,H, Ingles,Español,fuente)
from pyvidplayer import Video

# create display window


pantalla = pygame.display.set_mode((W, H))
pygame.display.set_caption('Monkey Guard')
icon = pygame.image.load('data/imagenes/icono.PNG').convert_alpha()
pygame.display.set_icon (icon)


pygame.init()
blanco = 255,255,255
negro= 0,0,0
pantalla= pygame.display.set_mode((1000, 600))
pygame.mixer.music.set_volume(0.0)
miFuente = pygame.font.Font(None, 35)
miTexto = miFuente.render("Presione P para saltar video", 1, (blanco))
vid = Video("naturaleza.mp4")
vid.set_size((1000, 550))
keys = pygame.key.get_pressed()


# load button images
level1_img = pygame.image.load('data/imagenes/nivel1.png').convert_alpha()
level2_img = pygame.image.load('data/imagenes/nivel2.png').convert_alpha()
level3_img = pygame.image.load('data/imagenes/nivel3.png').convert_alpha()
boton = pygame.image.load(variables.botonMorado).convert_alpha()
# create button instances
level3_button= button.Button(750,200, level3_img,0.8)
level2_button = button.Button(425, 190, level2_img, 0.9)
level1_button = button.Button(125, 200, level1_img, 0.8)
configuracion = button.Button(750,50,boton,0.7)
nivelFacil = button.Button(450, 450, boton, 0.6)
nivelDificil = button.Button(700, 440, boton, 0.8)
fondo = pygame.image.load("data/imagenes/fondoNiveles.png").convert_alpha()
fondoDificl = pygame.image.load("data/imagenes/Muerto.png").convert_alpha()
fD=False
# game loop
run = True
while run:
    pantalla.blit(fondoDificl,[0,0])
    if fD==True:
        pantalla.blit(fondo, [0, 0])   
    if not nivelFacil.draw(pantalla):
        pass
    else: 
        fD=False
        variables.dificil=False
    if not nivelDificil.draw(pantalla):
        pass
    else: 
        fD=True
        variables.dificil=True
    if not configuracion.draw(pantalla):
        pass
    else: 
        exec(open('./configuraciones.py', encoding="utf-8").read())
        sys.exit()
    if not level1_button.draw(pantalla):
        pass
    else:
        def intro():
            while True:
                pygame.init()
                pantalla.fill(negro)
                vid.draw(pantalla, (0, 0))
                pantalla.blit(miTexto, (50, 560))
                pygame.display.update()
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if keys[pygame.K_p]:
                        exec(open('./Juego1.py', encoding="utf-8").read())
                        pygame.quit()
                        vid.close()


        intro()
        sys.exit()
    if not level2_button.draw(pantalla):
        pass
    else:
        exec(open('./Juego2.py', encoding="utf-8").read())
        sys.exit()
    if not level3_button.draw(pantalla):
        pass
    else:
        exec(open('./Juego3.py', encoding="utf-8").read())
        sys.exit()

    if variables.botonR.draw(pantalla):
        exec(open('./button_main.py', encoding="utf-8").read())
        sys.exit()
    if variables.ingles ==True:
        pantalla.blit(fuente.render(Ingles[7],1,(0,0,0)), (160, 220))
        pantalla.blit(fuente.render(Ingles[8],1,(0,0,0)), (460, 220))
        pantalla.blit(fuente.render(Ingles[9],1,(0,0,0)), (780, 220))
        pantalla.blit(fuente.render(Ingles[1],1,(0,0,0)), (245, 465))
        pantalla.blit(fuente.render(Ingles[10],1,(0,0,0)), (767, 72))
        pantalla.blit(fuente.render(Ingles[13],1,(0,0,0)), (720, 470))
        pantalla.blit(fuente.render(Ingles[12],1,(0,0,0)), (495, 470))
        pantalla.blit(fuente.render(Ingles[14],1,(255,255,255)), (100,100))
    else:
        pantalla.blit(fuente.render(Español[7],1,(0,0,0)), (160, 220))
        pantalla.blit(fuente.render(Español[8],1,(0,0,0)), (460, 220))
        pantalla.blit(fuente.render(Español[9],1,(0,0,0)), (780, 220))
        pantalla.blit(fuente.render(Español[1],1,(0,0,0)), (232, 465))
        pantalla.blit(fuente.render(Español[10],1,(0,0,0)), (770, 72))
        pantalla.blit(fuente.render(Español[13],1,(0,0,0)), (765, 470))
        pantalla.blit(fuente.render(Español[12],1,(0,0,0)), (495, 470))
        pantalla.blit(fuente.render(Español[14],1,(255,255,255)), (50,100))
    if variables.dificil==True:
        if variables.ingles==True:
            pantalla.blit(fuente.render(Ingles[13],1,(255,255,255)), (500, 100))
        else:
            pantalla.blit(fuente.render(Español[13],1,(255,255,255)), (500, 100))
    else:
        if variables.ingles==True:
            pantalla.blit(fuente.render(Ingles[12],1,(255,255,255)), (500, 100))
        else:
            pantalla.blit(fuente.render(Español[12],1,(255,255,255)), (500, 100))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()

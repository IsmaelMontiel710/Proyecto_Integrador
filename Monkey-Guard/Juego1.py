import pygame,sys
from Jugador import jugador
from Mapa import Mapa
import variables
from variables import musica
from variables import (pantalla,negro,fps,reloj,Termino)
import button

pygame.display.set_caption('Nivel 1')
icon = pygame.image.load('data/imagenes/icono.PNG')
pygame.display.set_icon (icon)

imgObjecto="data/imagenes/panel.png"
p1 = "data/imagenes/pizo.png"
p2 = "data/imagenes/pizo2.png"
fondo = "data/imagenes/nivel1.png"


if variables.dificil==True:
    counter, text = 100, '100'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    fonNivel = "data/imagenes/fondoNivel1.png"
    Map = "nivel1.txt"
    Nivel=True
    Vidas=True
    Objeto = True
else:
    counter, text = 180, '180'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    fonNivel = "data/imagenes/fondoNivel1.png"
    Map = "nivel1.txt"
    Nivel=False
    Vidas=True
    Objeto = True
#Inicializar
mapa=Mapa()
monti = jugador()
musica = musica()
mapa.init(pantalla=pantalla, Nivel1=Nivel, Map=Map, Objet=Objeto, imgObjecto=imgObjecto)
monti.init(pantalla)

#Prueba

#fin prueba
while not Termino:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Termino = True
        if event.type == pygame.USEREVENT:
            counter -= 1
            
            text = str(counter).rjust(3) 
            if counter < 0 :
                exec(open('GameOver.py', encoding="utf-8").read())
        #Eventos
        monti.eventos(event, pantalla)
    
    # implementacion del sonido
    musica.Msonido()
    
    # Actualizacion de los sprite
    monti.actualizar()
    mapa.Actualizar(monti)
    pantalla.fill(negro)
    pantalla.blit(font.render(text, True, (255, 255, 255)), (10, 10))
    #Dibujar
    mapa.dibujar(pantalla, monti, fondo=fondo, p1=p1, p2=p2, fonNivel=fonNivel, Map=Map,incVidas=Vidas)
    monti.dibujar(pantalla)
    if variables.ingles==True:
        pantalla.blit(variables.fuente.render(variables.Ingles[7],1,(0,0,0)), (815, 20))
    else:
        pantalla.blit(variables.fuente.render(variables.Español[7],1,(0,0,0)), (815, 20))
    pygame.display.flip()
    reloj.tick(fps)
    keys = pygame.key.get_pressed()
	

    #Salir con boton Esc
    if keys[pygame.K_ESCAPE]:
        sys.exit()


# Salida del juego
pygame.quit()
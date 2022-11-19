import pygame,sys
from pygame import mixer
import button

pygame.init()
pantalla = pygame.display.set_mode((1000,600))
W,H = 1000,600
negro = (0, 0, 0)
fps=600
reloj = pygame.time.Clock()
Termino = False

Español= [
    "JUGAR",
    "SALIR",
    "VOLVER AL MENU",
    "VOLVER",
    "ESPAÑOL",
    "INGLES",
    "CONTROLES",
    "NIVEL 1",
    " NIVEL    2",
    "NIVEL 3",
    "AJUSTES",
    "GANASTE",
    "FACIL",
    "DIFICIL",
    "MODO DE DIFICULTAD:",
    "JUEGO EN PAUSA"
]
Ingles= [
    "PLAY",
    "QUIT",
    "RETURN TO MENU",
    "BACK",
    "SPANISH",
    "ENGLISH",
    "CONTROLS",
    "LEVEL 1",
    "LEVEL    2",
    "LEVEL 3",
    "SETTINGS",
    "WINNER",
    "EASY",
    "HARDCORE",
    "DIFFICULTY MODE:",
    "GAME PAUSED"
]
fuente = pygame.font.Font(None, 50)
ingles=False
dificil=False
botonM = button.Button(200, 350, pygame.image.load("data/imagenes/botonMorado.png").convert_alpha(), 0.6)
botonR = button.Button(200, 450, pygame.image.load("data/imagenes/botonRojo.png").convert_alpha(), 0.6)
botonMorado = "data/imagenes/botonMorado.png"
botonRojo = "data/imagenes/botonRojo.png"
class Imagenes:
    def nivel1():
        Montiparado = pygame.image.load('data/imagenes/quieto.png').convert_alpha
        Montiaire = pygame.image.load('data/imagenes/salto.png').convert_alpha
        MontiCaminando = pygame.image.load('data/imagenes/quieto.png').convert_alpha
        MontiCaminando = pygame.image.load('data/imagenes/caminando1.png').convert_alpha
        MontiCaminando = pygame.image.load('data/imagenes/caminando2.png').convert_alpha
class musica:
    
    # Inicializa la musica en bucle
    pygame.init()
    pygame.mixer.init(22050, -16, 2, 512)
    pygame.mixer.set_num_channels(32)
    # Musica agregada
    mixer.music.load('data/audio/fondo.wav')
    #El -1 sirve para hacer que se repita la cancion indefinidamente
    mixer.music.play(-1) 
    def Msonido(pantalla):
        
    	# Control del audio
        # key sirve para poder utilizar teclas del teclado
        keys = pygame.key.get_pressed()
	    # Baja volumen
        if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() -0.01)

        # Sube volumen
        if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        # Desactivar sonido
        elif keys[pygame.K_m]:
            pygame.mixer.music.set_volume(0.0)
        # Reactivar el sonido
        elif keys[pygame.K_COMMA]:
            pygame.mixer.music.set_volume(1.0)

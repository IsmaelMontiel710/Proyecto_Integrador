import pygame, sys
from objetos import objeto
import button
import variables
from Jugador import jugador
from enemigos import enemigo
tamano = 30
azul = (152, 217, 234)
verde = (0, 170, 0)
blanco = (255,255,255)
negro = (0, 0, 0)
hueso = (230, 214, 144)
VERDE = 0, 255, 0
H_FA2F2F = (250, 47, 47)
cafe = (128,64,0)
amarillo = (255,255,0)
naranja = (255,64,0)
verdee = (45,87,44)
transparemte=()

class Mapa:
    
    espacio = 0
    enemigos = []
    def init(self, pantalla ,Nivel1, Objet, Map, imgObjecto):
        mapa = open(Map, "r")
        if Nivel1 == True:
            for (idx, fila) in enumerate(mapa):
                for(idx2, col) in enumerate(fila):
                    posx = idx2 * tamano - self.espacio
                    posy = idx * tamano
                    if col == "r" or col == "e":
                        nuevo_enemigo = enemigo()
                        nuevo_enemigo.init(pantalla, posx, posy)
                        self.enemigos.append(nuevo_enemigo)
        if Objet == True:
            for (idx, fila) in enumerate(mapa):
                for(idx2, col) in enumerate(fila):
                    posx = idx2 * tamano - self.espacio
                    posy = idx * tamano
                    if col == "r" or col == "e":
                        nuevo_enemigo = objeto()
                        nuevo_enemigo.init(pantalla, posx, posy, imgObjecto)
                        self.enemigos.append(nuevo_enemigo)
        mapa.close()   
    def Actualizar (self, monti):

        for enem in self.enemigos:
            enem.actualizar(monti, self.espacio)
    def dibujar (self, pantalla, monti, fondo, p1, p2, fonNivel, Map, incVidas):
        self.piso = pygame.image.load(p1)
        self.piso2 = pygame.image.load(p2)
        #Probando
        self.pared = pygame.image.load("data/imagenes/muerto.png").convert_alpha()
        self.pared.set_colorkey((0, 0, 0))
        self.pared = self.pared.convert()
        self.muro = pygame.image.load("data/imagenes/muro_final.png").convert_alpha()
        self.muro.set_colorkey((0, 0, 0))
        self.muro = self.muro.convert()
        self.muro2 = pygame.image.load("data/imagenes/muro2.png").convert_alpha()
        self.muro2.set_colorkey((0, 0, 0))
        self.muro2 = self.muro2.convert()
        self.puerta = pygame.image.load("data/imagenes/puerta1.png").convert_alpha()
        self.puerta.set_colorkey((0, 0, 0))
        self.puerta = self.puerta.convert()
        self.tierra = pygame.image.load("data/imagenes/tierra.png").convert_alpha()
        self.tierra.set_colorkey((0, 0, 0))
        self.tierra = self.tierra.convert()
        paused = pygame.image.load("data/imagenes/Pause.png").convert_alpha()
        pa_button = button.Button(100, 4, paused, 0.8)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            pausa(pantalla)
        if not pa_button.draw(pantalla):
            pass
        else:
            pausa(pantalla)
        #Fin probando
        self.fondo = pygame.image.load(fondo).convert_alpha()
        fondoNivel = pygame.image.load(fonNivel).convert()
        x=0
        W = 1000
        x_relativa = x % fondoNivel.get_rect().width
        pantalla.blit(fondoNivel, (x_relativa - x % fondoNivel.get_rect().width, 72))
        if x_relativa < W:
            pantalla.blit(fondoNivel, (x_relativa, 72))
        x-=1
        y = 750
        if y < W:
            pantalla.blit(pygame.transform.scale(self.fondo,(260,70)), (y, 0))
            largo = 200
            ancho = 25
            ancho_corto = 19
            calcular_progreso = int((objeto.cantidad * largo / 8))
            borde_barra = pygame.Rect(150, 15, 206, ancho)
            rectangulo_barra = pygame.Rect(153, 18, calcular_progreso, ancho_corto)
            pygame.draw.rect(pantalla, VERDE, borde_barra, 3)
            pygame.draw.rect(pantalla, H_FA2F2F, rectangulo_barra)
            if objeto.cantidad > 2 and objeto.cantidad < 5:
                pygame.draw.rect(pantalla, VERDE, borde_barra, 3)
                pygame.draw.rect(pantalla, naranja, rectangulo_barra)
            if objeto.cantidad > 4 and objeto.cantidad < 7:
                pygame.draw.rect(pantalla, VERDE, borde_barra, 3)
                pygame.draw.rect(pantalla, amarillo, rectangulo_barra)
            if objeto.cantidad == 7 and objeto.cantidad < 8:
                pygame.draw.rect(pantalla, VERDE, borde_barra, 3)
                pygame.draw.rect(pantalla, verdee, rectangulo_barra)
        if monti.x > 650:
            monti.x = 650
            self.espacio += monti.velocidad
        if monti.x < 300 and self.espacio > 0:
            monti.x = 300
            self.espacio -= monti.velocidad
        if self.espacio < 0:
            self.espacio = 0
        self.warnig = pygame.image.load(("data/imagenes/corazon_perdido.png")).convert()
        self.warnig.set_colorkey((255,255,255))
        self.warnig = self.warnig.convert_alpha()
        if incVidas==True:
            if monti.vidas == 3:
                pantalla.blit(pygame.transform.scale(self.warnig, (25, 25)), (525, 15))
                pantalla.blit(pygame.transform.scale(self.warnig, (25, 25)), (545, 15))
                pantalla.blit(pygame.transform.scale(self.warnig, (25, 25)), (500, 15))
            if monti.vidas == 2:
                pantalla.blit(pygame.transform.scale(self.warnig, (25, 25)), (525, 15))
                pantalla.blit(pygame.transform.scale(self.warnig, (25, 25)), (545, 15))
            if monti.vidas == 1:
                pantalla.blit(pygame.transform.scale(self.warnig, (25, 25)), (525, 15))
            if monti.vidas == 0:
                exec(open('GameOver.py', encoding="utf-8").read())
        rect = monti.parado.get_rect(x=monti.x, y=monti.y)
        f = open(Map, "r")
        for (idx, fila) in enumerate(f):
            for(idx2, col) in enumerate(fila):
                posx = idx2 * 30 - self.espacio
                posy = idx * 30
                if col == "t":
                    bloque = pygame.draw.rect(pantalla, 0, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.pared, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if monti.direccion_actual == 1:
                                monti.x = posx - rect.width
                            else:
                                monti.x = posx + tamano * 1
                #Probando
                if col == "l":
                    rect = monti.parado.get_rect(x=monti.x, y=monti.y)
                    bloque = pygame.draw.rect(pantalla, verde, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.tierra, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.y + rect.height < posy + 10 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.tierra = True
                        elif rect.y > posy + tamano -20 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.velocidady = monti.gravedad
                        elif rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if monti.direccion_actual == 1:
                                monti.x = posx - rect.width
                            else:
                                monti.x = posx + tamano * 1

                if col == "g":
                    rect = monti.parado.get_rect(x=monti.x, y=monti.y)
                    bloque = pygame.draw.rect(pantalla, 0, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.muro, (tamano * 1, tamano)), (posx, posy))

                if col == "a":
                    rect = monti.parado.get_rect(x=monti.x, y=monti.y)
                    bloque = pygame.draw.rect(pantalla, 0, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.muro2, (tamano * 1, tamano)), (posx, posy))

                if col == "h":
                    pantalla.blit(pygame.transform.scale(self.puerta, (tamano * 1, tamano)), (posx, posy))
                #Fin prueba
                if col == "w" or col == "r":
                    bloque = pygame.draw.rect(pantalla, verde, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.piso, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.y + rect.height < posy + 10 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.tierra = True
                        elif rect.y > posy + tamano -20 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.velocidady = monti.gravedad
                        elif rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if monti.direccion_actual == 1:
                                monti.x = posx - rect.width
                            else:
                                monti.x = posx + tamano * 1
                if col == "d"  or col == "e":
                    bloque = pygame.draw.rect(pantalla, verde, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.piso2, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.y + rect.height < posy + 10 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.tierra = True
                        elif rect.y > posy + tamano -20 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.velocidady = monti.gravedad
                        elif rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if monti.direccion_actual == 1:
                                monti.x = posx - rect.width
                            else:
                                monti.x = posx + tamano * 1

        for enem in self.enemigos:
            enem.dibujar(pantalla, self.espacio)
        

        f.close()
def pausa(pantalla):
    miFuente = pygame.font.Font(None, 70)
    miFuente1 = pygame.font.Font(None, 35)
    miTexto1 = miFuente1.render("GAEL PONTE PILAS", 1, (blanco))
    # load button images
    fondo= pygame.image.load('data/imagenes/PantallaPause.png').convert_alpha()
    mute_img = pygame.image.load('data/imagenes/Mute.png').convert_alpha()
    exit_img = pygame.image.load('data/imagenes/Volumenon.png').convert_alpha()
    retornar = pygame.image.load('data/imagenes/Return.png').convert_alpha()
    nivel = pygame.image.load(variables.botonRojo).convert_alpha()
    continuar = pygame.image.load(variables.botonMorado).convert_alpha()
    # create button instances
    mute_button = button.Button(750, 70, mute_img, 0.8)
    son_button = button.Button(750, 175, exit_img, 0.8)
    ret_button = button.Button(50, 450, retornar, 0.8)
    nivel_button = button.Button(100, 415, nivel, 0.6)
    con_button = button.Button(400, 400, continuar, 1.1)


    pausado = True
    while pausado:
        pantalla.blit(fondo, [0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if not ret_button.draw(pantalla):
            pass
        else:
           return exec(open('./Juego1.py', encoding="utf-8").read())
        if not nivel_button.draw(pantalla):
            pass
        else:
            objeto.cantidad -= objeto.cantidad
            pygame.mixer.music.set_volume(0.0)
            exec(open('./Niveles.py', encoding="utf-8").read())
            sys.exit()
        if not con_button.draw(pantalla):
            pass
        else:
            pausado = False
        if not mute_button.draw(pantalla):
            pass
        else:
            pygame.mixer.music.set_volume(0.0)
        if son_button.draw(pantalla):
            pygame.mixer.music.set_volume(1.0)
        if variables.ingles==True:
            pantalla.blit(variables.fuente.render(variables.Ingles[2],1,(0,0,0)), (415, 445))
            pantalla.blit(variables.fuente.render(variables.Ingles[1],1,(0,0,0)), (140, 435))
            pantalla.blit(variables.fuente.render(variables.Ingles[15],1,(0,0,0)), (280, 100))
        else:
            pantalla.blit(variables.fuente.render(variables.Español[2],1,(0,0,0)), (415, 445))
            pantalla.blit(variables.fuente.render(variables.Español[1],1,(0,0,0)), (140, 435))
            pantalla.blit(variables.fuente.render(variables.Español[15],1,(0,0,0)), (280, 100))
        pantalla.blit(miTexto1, (300, 250))
        pygame.display.update()
        reloj.tick(5)



reloj = pygame.time.Clock()
Termino = False

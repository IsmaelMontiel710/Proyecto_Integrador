import pygame,sys
from Jugador import jugador
class enemigo(pygame.sprite.Sprite):
    x = 0
    y = 0
    pos_inicial = 0
    velocidad = 0
    imagenes = []
    amplitud = 0
    cuadro_actual = 0
    contador = 0
    muerto = False
    origy = 0
    def init(self, pantalla, x, y):
        self.muerto = False
        self.cuadro_actual = 0
        self.x = x
        self.post_inicial = x
        self.velocidad = 5
        self.imagenes.append(pygame.image.load('data/imagenes/slime1.png').convert_alpha(pantalla))
        self.imagenes.append(pygame.image.load('data/imagenes/slime2.png').convert_alpha(pantalla))
        self.imagenes.append(pygame.image.load('data/imagenes/slime3.png').convert_alpha(pantalla))
        self.imagenes.append(pygame.image.load('data/imagenes/slime4.png').convert_alpha(pantalla))
        self.imagenes.append(pygame.image.load('data/imagenes/muerto1.png').convert_alpha(pantalla))
        self.imagenes.append(pygame.image.load("data/imagenes/muerto.png").convert_alpha(pantalla))
        for imagen in self.imagenes:
            imagen.set_colorkey((255, 255, 255))
        self.amplitud = self.imagenes[0].get_width()
        self.origy = y
        self.y = self.origy - self.imagenes[0].get_height()
    def actualizar(self, monti, espacio):
        if self.muerto == True:
            self.cuadro_actual = 5
        if not self.muerto:
            self.contador += 1
            if self.contador > 10:
                self.contador = 0
                self.cuadro_actual += 1
                if self.cuadro_actual > 3:
                    self.cuadro_actual = 0
            self.x -= self.velocidad
            if self.x - espacio < self.post_inicial - espacio - 100 or self.x - espacio > self.post_inicial-espacio + 100 + self.amplitud:
                self.velocidad = -self.velocidad
            bloque = self.imagenes[0].get_rect(x=self.x - espacio, y=self.y)
            rect = monti.parado.get_rect(x=monti.x, y=monti.y)
            contador = 0
            if bloque.colliderect(rect):
                if rect.y + rect.height > bloque.y + 10:
                    monti.vidas -= 1
                    monti.y = 518
                    monti.x = 50
                if rect.x + rect.height < bloque.y + 10 and rect.x + rect.width > bloque.x and rect.x < bloque.x + bloque.width:
                    self.muerto = True
                    self.cuadro_actual = 4
                if rect.y + rect.height < bloque.y + 10 and rect.x + rect.width > bloque.x and rect.x < bloque.x + bloque.width:
                    self.muerto = True
                    self.cuadro_actual = 4
        self.y = self.origy - self.imagenes[self.cuadro_actual].get_height()
    
    def dibujar(self, pantalla, espacio):
        pantalla.blit(self.imagenes[self.cuadro_actual], (self.x - espacio, self.y) )
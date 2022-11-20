import pygame
VERDE = 0,255,0
H_FA2F2F = (250, 47, 47)

class objeto:
    x = 0
    y = 0
    pos_inicial = 0
    imagenes = []
    amplitud = 0
    cuadro_actual = 0
    contador = 0
    muerto = False
    origy = 0
    cantidad = 0

    def init(self, pantalla, x, y, imgObjecto):
        self.muerto = False
        self.cuadro_actual = 0
        self.x = x
        self.post_inicial = x
        self.velocidad = 5
        self.imagenes.append(pygame.image.load(imgObjecto).convert_alpha(pantalla))
        self.imagenes.append(pygame.image.load('data/imagenes/muerto.png').convert_alpha(pantalla))
        for imagen in self.imagenes:
            imagen.set_colorkey((0, 0, 0))
        self.amplitud = self.imagenes[0].get_width()
        self.origy = y
        self.y = self.origy - self.imagenes[0].get_height()

    def actualizar(self, monti, espacio):
        if not self.muerto:
            self.contador += 1
            if self.contador > 10:
                self.contador = 0
                self.cuadro_actual += 1
                if self.cuadro_actual == 1:
                    self.cuadro_actual = 0

            bloque = self.imagenes[0].get_rect(x=self.x - espacio, y=self.y)
            rect = monti.parado.get_rect(x=monti.x, y=monti.y)
            if bloque.colliderect(rect):
                objeto.cantidad += 1
                if rect.y + rect.height < bloque.x + 10 and rect.y + rect.width > bloque.y and rect.y < bloque.y + bloque.width:
                    self.muerto = True
                    self.cuadro_actual = 1
                if rect.x + rect.height < bloque.x + 10 and rect.y + rect.width > bloque.y and rect.y < bloque.y + bloque.width:
                    self.muerto = True
                    self.cuadro_actual = 1
                if objeto.cantidad == 8:
                    objeto.cantidad -= 8
                    exec(open('ganador.py', encoding="utf-8").read())

        self.y = self.origy - self.imagenes[self.cuadro_actual].get_height()
    
    def dibujar(self, pantalla, espacio):
        pantalla.blit(self.imagenes[self.cuadro_actual], (self.x - espacio, self.y) )
        
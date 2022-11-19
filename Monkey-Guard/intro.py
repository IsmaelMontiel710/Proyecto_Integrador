import pygame

from pyvidplayer import Video

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
                exec(open('./Juego3.py', encoding="utf-8").read())
                vid.close()



intro()

pygame.quit()
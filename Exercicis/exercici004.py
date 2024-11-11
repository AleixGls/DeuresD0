#---|IMPORTACIONS|-----------------------------------------------------------------------------------
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import utils
import sys
import random

#---|COLORS|-----------------------------------------------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PINK = (255, 105, 180)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


pygame.init()
clock = pygame.time.Clock()

#---|FINESTRA|---------------------------------------------------------------------------------------
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

#---|APLICACIO|--------------------------------------------------------------------------------------
def main():
    global coordenades

    window_width, window_height = screen.get_size()
    coordenades = []
    for i in range(10):
        coordenades.append(
            (random.randint(0, window_width), 
            random.randint(0, window_height))
        )

    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

#---|EVENTS|-----------------------------------------------------------------------------------------
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

#---|CALCULS|----------------------------------------------------------------------------------------
def app_run():
    pass

#---|DIBUIX|-----------------------------------------------------------------------------------------
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    pygame.draw.polygon(screen, BLACK, coordenades, 5)

    pygame.display.update()

#---|INICIAR|----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
#---|IMPORTACIONS|-----------------------------------------------------------------------------------
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import utils
import sys

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

direccio = "none"

pos_x = 100
size = 25

#---|FINESTRA|---------------------------------------------------------------------------------------
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

#---|APLICACIO|--------------------------------------------------------------------------------------
def main():
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
    global direccio

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.KEYDOWN:  # Tecla premuda
            if event.key == pygame.K_LEFT:
                direccio = 'left'
            elif event.key == pygame.K_RIGHT:
                direccio = 'right'
        elif event.type == pygame.KEYUP:  # Tecla alliberada
            if event.key == pygame.K_LEFT:
                if direccio == 'left':
                    direccio = 'none'
            elif event.key == pygame.K_RIGHT:
                if direccio == 'right':
                    direccio = 'none'
    return True

#---|CALCULS|----------------------------------------------------------------------------------------
def app_run():
    global pos_x, size

    delta_time = clock.get_time() / 1000.0  # Convertir a segons
    velocitat = 100
    des = velocitat * delta_time

    limit_r = screen.get_width()

    if direccio == "left":
        if pos_x - size <= 0:
            direccio == "none"
        else:
            pos_x -= des
            size = 10 + (pos_x / 8)
    elif direccio == "right":
        if pos_x + size >= limit_r:
            direccio == "none"
        else:
            pos_x += des
            size = 10 + (pos_x / 8) 

#---|DIBUIX|-----------------------------------------------------------------------------------------
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    fontArial = pygame.font.SysFont("Arial", 23)
    text = fontArial.render("Apreta les tecles (left/right)", True, BLACK)
    screen.blit(text, (50,50))

    pygame.draw.circle(screen, BLACK, (pos_x,250), size)

    pygame.display.update()

#---|INICIAR|----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
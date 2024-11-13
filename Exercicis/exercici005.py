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

    center_x, center_y = int(screen.get_width() / 2), int(screen.get_height() / 2)
    x, y = center_x, center_y
    step = 15
    direction = 0

    for _ in range(25):  
        if direction == 0:
            end_x, end_y = x + step, y
        elif direction == 1:
            end_x, end_y = x, y - step
        elif direction == 2:
            end_x, end_y = x - step, y
        elif direction == 3:
            end_x, end_y = x, y + step
        
        pygame.draw.line(screen, RED, (x, y), (end_x, end_y), 4)
        
        x, y = end_x, end_y
        direction = (direction + 1) % 4
        step += 15

    pygame.display.update()

#---|INICIAR|----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
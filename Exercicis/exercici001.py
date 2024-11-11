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

    fontArial1 = pygame.font.SysFont("Arial", 60)
    fontArial2 = pygame.font.SysFont("Arial", 28)
    fontCourier = pygame.font.SysFont("Courier New", 40, True)


    pygame.draw.rect(screen, RED, (50,50 , 550,100))
    text = fontArial1.render("HEADLINE NEWS", True, WHITE)
    screen.blit(text, (100, 70))

    text = fontCourier.render("World goes Wrong!", True, BLACK)
    screen.blit(text, (50, 150))

    text = fontCourier.render("YEP#", True, (100, 150, 100))
    screen.blit(text, (500, 150))

    text = fontArial2.render("Lorem ipsum dolor sit amet, consectetur",True, BLACK)
    screen.blit(text, (50, 250))
    text = fontArial2.render("adipiscing elit, sed do eiusmod tempor",True, BLACK)
    screen.blit(text, (50, 285))
    text = fontArial2.render("incididunt ut labore et dolore magna aliqua.",True, BLACK)
    screen.blit(text, (50, 320))

    pygame.display.update()

#---|INICIAR|----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
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
dades = [ 
  {'nom': 'Pelut', 'any': 2018, 'pes': 6.5, 'especie': 'Gos'},
  {'nom': 'Pelat', 'any': 2020, 'pes': 5.0, 'especie': 'Gos'},
  {'nom': 'Mia', 'any': 2022, 'pes': 3.0, 'especie': 'Gat'},
  {'nom': 'Nemo', 'any': 2003, 'pes': 0.1, 'especie': 'Peix'},
  {'nom': 'Mickey', 'any': 1928, 'pes': 0.5, 'especie': 'Ratolí'},
  {'nom': 'Donald', 'any': 1934, 'pes': 0.5, 'especie': 'Ànec'} 
]

def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    fontArial1 = pygame.font.SysFont("Arial", 18)
    fontArial2 = pygame.font.SysFont("Arial", 16)

    y=100
    for q in range (0, len(dades)):
        pygame.draw.rect(screen, WHITE, (150,y, 200,25),)
        pygame.draw.line(screen, BLACK, (150,y), (350,y),2)

        text = fontArial1.render(dades[q]["nom"], True, BLACK)
        screen.blit(text, (155, y+2))

        text = fontArial2.render(str(dades[q]["any"]), True, (50,120,200))
        screen.blit(text, (255, y+2))

        text = fontArial2.render(dades[q]["especie"], True, (50,120,200))
        screen.blit(text, (305, y+2))

        y += 25
        pygame.draw.line(screen, BLACK, (150,y), (350,y),2)

    pygame.display.update()

#---|INICIAR|----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
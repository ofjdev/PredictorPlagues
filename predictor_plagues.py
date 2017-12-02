import pygame
import random

# EXAMPLE TAKEN FROM:
# https://tpec05.blogspot.com.es/2016/02/programando-una-cuadricula-grid-en.html

blueP = (20, 34, 238)
greenP = (20, 240, 50)
redP = (230, 0, 20)
BLACK = (0, 0, 0)
sizeSquare = 40
px = int(raw_input("Coordenada en X: "))
py = int(raw_input("Coordenada en Y: "))

x = 0
y = 0
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(BLACK)
    Fuente = pygame.font.Font(None, 16)
    Tx = 0
    Ty = 0
    for i in range(1, size[0], 40):
        for j in range(1, size[1], 40):
            pygame.draw.rect(screen, blueP, [i, j, 38, 38], 0)
            if py == 0:
                y = 1
            elif py == Ty:
                y = j
            Ty += 1
        if px == 0:
            x = 1
        elif px == Tx:
            x = i
        Texto = Fuente.render(str(Tx), True, greenP)
        screen.blit(Texto, [i, 2])
        if Tx != 0:
            screen.blit(Texto, [2, i + 16])
        Tx += 1
        Ty = 0
    colAl = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
    pygame.draw.rect(screen, colAl, [x, y, 38, 38], 0)
    pygame.display.flip()
    clock.tick(5)
pygame.quit()
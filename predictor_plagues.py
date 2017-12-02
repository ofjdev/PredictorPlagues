import pygame
import random

# EXAMPLE TAKEN FROM:
# https://tpec05.blogspot.com.es/2016/02/programando-una-cuadricula-grid-en.html

blueP = (20, 34, 238)
greenP = (20, 240, 50)
green_chartreuse = (127, 255, 0)
redP = (230, 0, 20)
BLACK = (0, 0, 0)
sizeSquare = 40

x = 0
y = 0
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(BLACK)
    
    Tx = 0
    Ty = 0
    for i in range(1, size[0], 40):
        for j in range(1, size[1], 40):
            color_to_fill = greenP if (((j-1) // 40) % 2 == 1) else green_chartreuse
            pygame.draw.rect(screen, color_to_fill, [i, j, 37, 37], 0)
            Ty += 1
        Tx += 1
        Ty = 0
    colAl = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
    #pygame.draw.rect(screen, colAl, [x, y, 38, 38], 0)
    pygame.display.flip()
    #clock.tick(5)
pygame.quit()
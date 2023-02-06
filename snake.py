import pygame
from random import randrange

RES = 700
SIZE = 50
x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
length = 2
shake = [(x, y)]
dx, dy = 0, 0
fps = 5
pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
while 1:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1))) for i, j in shake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
    x += dx * SIZE
    y += dy * SIZE
    shake.append((x, y))
    shake = shake[-length:]
    if shake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
    pygame.display.flip()
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                dx, dy = 1, 0
            elif event.key == pygame.K_a:
                dx, dy = -1, 0
            elif event.key == pygame.K_w:
                dx, dy = 0, -1
            elif event.key == pygame.K_s:
                dx, dy = 0, -1

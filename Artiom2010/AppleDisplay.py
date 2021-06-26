import pygame
import random
import pygame as pg
import sys

pygame.init()
pygame.mixer.init()

w = 1680
h = 1020
FPS = 60
clock = pg.time.Clock()


apple = pygame.image.load("apple.png")

screen = pygame.display.set_mode((w, h))
x = 875
y = 375

game = True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
        else:
            screen.blit(apple, (400, 200))
pg.display.update()






















import pygame
import random
import pygame as pg
import sys

pygame.init()
pygame.mixer.init()

w = 1680
h = 900
FPS = 60
clock = pg.time.Clock()


fon = pygame.image.load("Fon.png")

screen = pygame.display.set_mode((w, h))
x = 0
y = 0

game = True
while game:
    screen.blit(fon, (x, y))
    pg.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False























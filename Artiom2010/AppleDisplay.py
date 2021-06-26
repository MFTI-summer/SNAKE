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

area = pg.image.load("Area.png")
apple = pg.image.load("apple.png")
snake = pg.image.load("Snake.bmp")
screen = pygame.display.set_mode((w, h))

x = 875
y = 375

game = True
while game:
    screen.blit(apple, (400, 200))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

pg.display.update()






















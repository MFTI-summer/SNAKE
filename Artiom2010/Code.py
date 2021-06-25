import pygame
import random
import pygame as pg
import sys
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("anotherday.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)
w = 1680
h = 900
FPS = 60
clock = pygame.time.Clock()
area = pg.image.load("Area.png")
snake = pg.image.load("Snake.bmp")
screen = pygame.display.set_mode((w, h))
x = 100
y = 100

game = True
while game:
    screen.blit(area, (500, 100))
    screen.blit(snake, (875, 375))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
pygame.quit()

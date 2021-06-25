import pygame
import random
import pygame as pg
import sys
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("anotherday.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)
WIDTH = 800
HEIGHT = 600
FPS = 60
area = pg.image.load("Area.bmp")
screen = pygame.display.set_mode((1680,1020))
x = 100
y = 100
screen.blit(area, (300, 300))
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
pygame.quit()

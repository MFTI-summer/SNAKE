import pygame
import random
import pygame as pg
import sys
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("anotherday.ogg")
pygame.mixer.music.load("darkside.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)
WIDTH = 800
HEIGHT = 600
FPS = 60
area = pg.image.load("Area.bmp")
screen = pygame.display.set_mode((1680,1020))
pygame.display.set_caption("Area.bmp")
clock = pygame.time.Clock()
x = 100
y = 100
game = True
while game:
    for event in pygame.event.get():
        screen.blit(area, (x, y))
        if event.type == pygame.QUIT:
            game = False
pygame.quit()

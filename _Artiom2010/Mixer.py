import pygame
import random
import pygame as pg
import sys

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("music1.ogg")
mt = 1
pygame.mixer.music.play(loops=1)
w = 1680
h = 1020
FPS = 60
clock = pg.time.Clock()


apple = pygame.image.load("apple.png")

screen = pygame.display.set_mode((w, h))
x = 825
y = 400

game = True
while game:
    screen.blit(apple, (x, y))
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.unload()
        print(mt)
        if mt >= 3:
            mt = 0
        nm = "music"+str(mt+1)+".ogg"
        mt = mt+1
        pygame.mixer.music.load(nm)
        pygame.mixer.music.play(loops=1)
    pg.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

import pygame
import random
import pygame as pg
import sys

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(1)
pygame.mixer.music.load("musictest1.ogg")
pygame.mixer.music.play(loops=1)
pygame.mixer.music.queue("musictest2.ogg")
pygame.mixer.music.play(loops=1)
pygame.mixer.music.queue("musictest3.ogg")
pygame.mixer.music.play(loops=1)
pygame.mixer.music.queue("musictest4.ogg")
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
    pg.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

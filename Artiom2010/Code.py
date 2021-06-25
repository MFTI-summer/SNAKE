import pygame
import random
import pygame as pg
import sys

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("anotherday.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)


WIDTH = 1680
HEIGHT = 1020
FPS = 60

clock = pygame.time.Clock()
area = pg.image.load("Area.png")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

x = 100
y = 100
screen.blit(area, (300, 300))


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("SPACE"*20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("SPACE")

    pygame.display.update()
pygame.quit()

import pygame
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("anotherday.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)
WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Area")
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

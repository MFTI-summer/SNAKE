import pygame as pg
import sys

FPS = 60
width = 800   #   длина и ширина окна
height = 600
x = 300     #  координаты верхней точки квадрата
y = 250


clock = pygame.time.Clock()
sc = pygame.display.set_mode((width, height))

sc.fill((255, 255, 255))

pg.draw.rect(sc, (255, 0, 0), (x, y, 85, 85), 10)





    


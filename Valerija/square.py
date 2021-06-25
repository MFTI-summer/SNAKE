import pygame as pg
import sys

FPS = 60

pg.init()
sc = pg.display.set_mode((800, 600))

pg.display.update()

pg.draw.rect(sc, (255, 0, 0), (150, 20, 150, 85), 10)

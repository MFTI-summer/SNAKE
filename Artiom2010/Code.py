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
x = 875
y = 375
spedx = 0
spedy = 0
PUR = (255, 255, 255)
sc = pg.display.set_mode ((w,h))
pygame.draw.rect(sc, PUR, (x, y, 50, 50), 8)
game = True
while game:
    screen.blit(area, (500, 100))
    screen.blit(snake, (875, 375))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
        elif i.type == pg.KEYDOWN:
                if i.key == pg.K_LEFT:
                    x -= 15
                elif i.key == pg.K_RIGHT:
                    x += 15
                elif i.key == pg.K_UP:
                    y -= 15
                elif i.key == pg.K_DOWN:
                    y += 15
    sc.fill((0,0,0))
    pygame.draw.rect(sc, PUR, (x, y, 50, 50), 8)
    pygame.display.update()
pygame.quit()

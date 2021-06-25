import pygame as pg
import sys

#### from pygame.locals import * - чтобы меньше писать


pg.init()

### ЭКРАН
W = 1000  # ширина
H = 800  # высота
sc = pg.display.set_mode((W, H))  # длина высота окна

# FPS
FPS = 60
clock = pg.time.Clock()

# SNAKE HEAD ГОЛОВА ЗМЕИ
x = 480
y = 350
PUR = (100, 128, 255)  #ЦВЕТ ЗМЕИ

speed_x = 0
speed_y = 0




while True:

    for i in pg.event.get():  # в пг из папки ивент фн гет, присваиает перем зн
        if i.type == pg.QUIT:
            sys.exit()  # кнц
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                x -= 15
            elif i.key == pg.K_RIGHT:
                x += 15
            elif i.key == pg.K_UP:
                y -= 15
            elif i.key == pg.K_DOWN:
                y += 15

    sc.fill((0, 0, 0))
    pg.draw.rect(sc, PUR, (x, y, 60, 60), 8)
    clock.tick(FPS)  # задержка

    pg.display.update()  # обновление экрана

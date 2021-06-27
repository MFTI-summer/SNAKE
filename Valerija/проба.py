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

PUR = (100, 128, 255)  #ЦВЕТ ЗМЕИ
a = 480
b = 350
pg.draw.rect(sc, PUR, (a, b, 60, 60), 8)
apple = pg.draw.circle(sc, (255, 0,0), (100, 100), 30)


speed_x = 0
speed_y = 0




while True:
    clock.tick(FPS)  # задержка


    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()  # кнц
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                if a > 0:
                    a = -20


            elif i.key == pg.K_RIGHT:
                if a < 940:
                    a += 20

            elif i.key == pg.K_UP:
                if b > 0:
                    b -= 20

            elif i.key == pg.K_DOWN:
                if b < 740:
                 b += 20



    sc.fill((0, 0, 0))
    pg.draw.rect(sc, PUR, (a, b, 60, 60), 8)
    pg.draw.circle(sc, (255,0,0),  apple.center, apple.width//2 )


    pg.display.update()  # обновление экрана

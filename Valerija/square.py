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
x = 480
y = 350
head = pg.draw.rect(sc, PUR, (x, y, 60, 60), 8)
apple = pg.draw.circle(sc, (255, 0,0), (100, 100), 30)


speed_x = 0
speed_y = 0




while True:
    clock.tick(FPS)  # задержка


    for i in pg.event.get():  # в пг из папки ивент фн гет, присваиает перем зн
        if i.type == pg.QUIT:
            sys.exit()  # кнц
        elif i.type == pg.KEYDOWN:                     #   не знаю, как связать со скоростью границы
            if i.key == pg.K_LEFT:
                if x > 0:
                    speed_x = -5
                else:
                    speed_x = 0

            elif i.key == pg.K_RIGHT:
                if x < 1000:
                    speed_x = 5
                else:
                    speed_x = 0

            elif i.key == pg.K_UP:
                if y > 0:
                    speed_y = -5
                else:
                    speed_y = 0

            elif i.key == pg.K_DOWN:
                if y < 800:
                    speed_y = 5
                else:
                    speed_y = 0



    head.x += speed_x
    head.y += speed_y

    sc.fill((0, 0, 0))
    pg.draw.rect(sc, PUR, head, 8)
    pg.draw.circle(sc, (255,0,0),  apple.center, apple.width//2 )



    pg.display.update()  # обновление экрана



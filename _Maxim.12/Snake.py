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

# snake HEAD ГОЛОВА ЗМЕИ

PUR = (100, 128, 255)  #ЦВЕТ ЗМЕИ

head = pg.draw.rect(sc, PUR, (480, 350, 60, 60), 8)
apple = pg.draw.circle(sc, (255, 0,0), (100, 100), 30)


speed_x = 0
speed_y = 0
count = 1 # кол-во съеденных яблок



while True:
    clock.tick(FPS)  # задержка


    for i in pg.event.get():  # в пг из папки ивент фн гет, присваиает перем зн
        if i.type == pg.QUIT:
            sys.exit()  # кнц
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                speed_x = -5

            elif i.key == pg.K_RIGHT:
                speed_x = 5

            elif i.key == pg.K_UP:
                speed_y = -5
            elif i.key == pg.K_DOWN:
                speed_y = 5

    head.x += speed_x
    head.y += speed_y

    sc.fill((0, 0, 0))
    pg.draw.rect(sc, PUR, head, 8)
    pg.draw.circle(sc, (255,0,0),  apple.center, apple.width//2 )


    f1 = pg.font.Font(None, 36) # выводит на экран надпись 'Score:'
    text1 = f1.render('Score:', True, (255, 255, 0))
    sc.blit(text1, (900,50))
    f2 = pg.font.Font(None, 36)
    text2 = f2.render(str(count), True, (255, 255, 0))
    sc.blit(text2, (980,50))



    pg.display.update()  # обновление экрана

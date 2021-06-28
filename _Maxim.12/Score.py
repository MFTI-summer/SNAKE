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
count = 1 # кол-во съеденных яблок
while True:
    clock.tick(FPS)  # задержка


    for i in pg.event.get():  # в пг из папки ивент фн гет, присваиает перем зн
        if i.type == pg.QUIT:
            sys.exit()  # кнц
    f1 = pg.font.Font(None, 36) # выводит на экран надпись 'Score:'
    text1 = f1.render('Score:', True, (255, 255, 0))
    sc.blit(text1, (900, 50))
    f2 = pg.font.Font(None, 36)
    text2 = f2.render(str(count), True, (255, 255, 0))
    sc.blit(text2, (980, 50))



    pg.display.update()  # обновление экрана

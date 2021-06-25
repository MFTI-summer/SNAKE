import pygame as pg
import sys
#### from pygame.locals import * - чтобы меньше писать

FPS = 60
W = 1000 #ширина
H = 800 #высота
x = 480
y = 350
PUR = (100, 128, 255)

pg.init()
sc = pg.display.set_mode ((W,H)) #длина высота окна
pg.draw.rect(sc, PUR, (x, y, 60, 60), 8)

clock = pg.time.Clock()



pg.display.update() #обновление экрана


while True:

 for i in pg.event.get(): #в пг из папки ивент фн гет, присваиает перем зн
  if i.type == pg.QUIT:
    sys.exit()  #кнц
  elif i.type == pg.KEYDOWN:
    if i.key == pg.K_LEFT:
                x -= 3
    elif i.key == pg.K_RIGHT:
                x += 3

 pg.draw.rect(sc, PUR, (x, y, 60, 60), 8)
 clock.tick(FPS) #задержка


pg.display.update()




import pygame as pg
# import sys

FPS = 60
width = 800   #   длина и ширина окна
height = 600
x = 300     #  координаты верхней точки квадрата
y = 250


# clock = pg.time.Clock()
sc = pg.display.set_mode((width, height))  #Создание И настройка размеров экрана

sc.fill((255, 255, 255))  #Заливаем экран белым цветом

game = True
while game:
    for event in pg.event.get():
        print(event)
        if event.type == pg.QUIT:
            game = False

    pg.display.update()    #  обновление экрана
    pg.draw.rect(sc, (255, 0, 0), (x, y, 150, 85), 10)
pg.quit()



import pygame as pg
import sys

W = 1000  # ширина
H = 800  # высота
sc = pg.display.set_mode((W, H))  # длина высота окна

x1, x2 = 5, W - 5    #  координаты границ
y1, y2 = 5, H - 150

PUR = (100, 128, 255)  #ЦВЕТ ЗМЕИ

h_border = pg.sprite.Group() #группа спрайтов - горизонаьльные препятствия
v_border = pg.sprite.Group() #группа спрайтов - вертикальные стенки


# горизонтальная стенка
class Borderh(pg.sprite.Sprite): # создаем класс Sprite
    def __init__(self, x1, y1, x2, y2):
        super().__init__(h_border)
        self.add(h_border)
        self.rect = pg.Rect(x1, y1, x2 - x1, 1)

# вертикальная стенка
class Borderv(pg.sprite.Sprite): # создаем класс Sprite
    def __init__(self, x1, y1, x2, y2):
        super().__init__(v_border)
        self.add(v_border)
        self.rect = pg.Rect(x1, y1, 1, y2 - y1)

class Player(pg.sprite.Sprite):
    def __init__(self):
        self.image = pg.Surface((60, 60))
        self.image.fill(PUR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        if x > 0:
            self.speed_x = -10
        elif x < 1000:
            self.speed_x = 10
        elif y > 0:
            self.speed_y = -10
        elif y < 800:
            self.speed_y = 10

        self.rect = self.rect.move(self.speed_x, self.speed_y) #  шаг спрайта
        if pg.sprite.spritecollideany(self, h_border): # проверяем столкновение мяча с группой спрайтов "горизонтальные препятствия"
            self.speed_x = -self.speed_x
        if pg.sprite.spritecollideany(self, v_border): # проверяем столкновение мяча с группой спрайтов "вертикальные стенки"
            self.speed_y = -self.speed_y


pg.init()

sc = pg.display.set_mode((W, H))  # длина высота окна

Borderh(x1, y1, x2, y1)
Borderh(x1, y2, x2, y2)
Borderv(x1, y1, x1, y2)
Borderv(x2, y1, x2, y2)


# FPS
FPS = 60
clock = pg.time.Clock()

# SNAKE HEAD ГОЛОВА ЗМЕИ
apple = pg.draw.circle(sc, (255, 0,0), (100, 100), 30)

while True:
    clock.tick(FPS)  # задержка


    for i in pg.event.get():  # в пг из папки ивент фн гет, присваиает перем зн
        if i.type == pg.QUIT:
            sys.exit()  # кнц
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                self.speed_x = -10

            elif i.key == pg.K_RIGHT:
                self.speed_x = 10

            elif i.key == pg.K_UP:
                self.speed_y = -10
            elif i.key == pg.K_DOWN:0
                self.speed_y = 10

    pg.all_sprites.update()
    sc.fill((0, 0, 0))
    pg.draw.circle(sc, (255,0,0),  apple.center, apple.width//2 )

    pg.display.update()  # обновление экран


pygame.quit()

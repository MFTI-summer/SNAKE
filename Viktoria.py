import pygame
import sys
#### from pygame.locals import * - чтобы меньше писать

FPS = 60
W = 1000 #ширина
H = 800 #высота
x = 480
y = 350
PUR = (100, 128, 255)

pygame.init()
sc = pygame.display.set_mode ((W,H)) #длина высота окна
pygame.draw.rect(sc, PUR, (x, y, 60, 60), 8)

clock = pygame.time.Clock()



pygame.display.update() #обновление экрана


while True:

    for i in pygame.event.get():  # в пг из папки ивент фн гет, присваиает перем зн
        if i.type == pygame.QUIT:
            sys.exit()  # кнц
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 15
            elif i.key == pygame.K_RIGHT:
                x += 15
            elif i.key == pygame.K_UP:
                y -= 15
            elif i.key == pygame.K_DOWN:
                y += 15


    sc.fill((0,0,0))
    pygame.draw.rect(sc, PUR, (x, y, 60, 60), 8)
    clock.tick(FPS)  # задержка


    pygame.display.update()




import pygame
import sys

FPS = 60
width = 800   #   длина и ширина окна
height = 600
x = 300     #  координаты верхней точки квадрата
y = 250


clock = pygame.time.Clock()
sc = pygame.display.set_mode((width, height))

sc.fill((255, 255, 255))

pygame.draw.rect(sc, (255, 0, 0), (x, y, 85, 85), 10)


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -=30
            elif i.key == pygame.K_RIGHT:
                x +=30
            elif i.type == pygame.K_UP:
                y -=30
            elif i.key == pygame.K_DOWN:
                y +=30


    pygame.draw.rect(sc, (255, 0, 0) , (x, y, 85, 85), 10)
    pygame.display.update()
    clock.tick(FPS)








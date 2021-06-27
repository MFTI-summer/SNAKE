import pygame
from pygame import*
move_speed = 5
a = 800 #длина
b = 400 #ширина
c = (200, 200, 200)#цвет

def screen():
    pygame.init()
    display = pygame.display.set_mode((a, b))
    cube = pygame.Surface((100, 100))
    display.fill(Color(c))

 while :
        for i in pygame.event.get(): # Обрабатываем события

            if i.type == QUIT:

                raise SystemExit("QUIT")



        display.blit(display, (0, 0))
        display.blit(cube,(400, 200))
        pygame.display.update()

screen()


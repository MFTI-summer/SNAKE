import pygame
import sys


#   ЭКРАН
FPS = 60
width = 800  # ширина экрана
height = 600 # высота экрана
white= (255, 255, 255)

sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# координаты и радиус круга
pink = (255, 150, 255)
x = width/2
y = height/2
r = 40

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 15
            elif i.key == pygame.K_RIGHT:
                x += 15
            elif i.key == pygame.K_UP:
                y -=15
            elif i.key == pygame.K_DOWN:
                y +=15

    sc.fill(white)
    pygame.draw.circle(sc, pink, (x, y), r)
    pygame.display.update()
    clock.tick(FPS)

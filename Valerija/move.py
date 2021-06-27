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
    keys = pygame.key.get_pressed()      #тут сделаны границы
    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= 10
    if keys[pygame.K_RIGHT]:
        if x < 800:
            x += 10
    if keys[pygame.K_UP]:
        if y > 0:
            y -= 10
    if keys[pygame.K_DOWN]:
        if y < 600:
            y += 10

    sc.fill((255, 255, 255))
    pygame.draw.circle(sc, pink, (x, y), r)
    pygame.display.update()
    clock.tick(FPS)

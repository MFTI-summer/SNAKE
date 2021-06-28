import pygame
import random
import pygame as pg
import sys

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("anotherday.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)


w = 1680
h = 1020
FPS = 60

clock = pygame.time.Clock()
area = pg.image.load("Area.png")
apple = pg.image.load("apple.png")
snake = pg.image.load("Snake.bmp")
screen = pygame.display.set_mode((w, h))
x = 875
y = 375
spedx = 0
spedy = 0
PUR = (255, 255, 255)
sc = pg.display.set_mode ((w,h))
pygame.draw.rect(sc, PUR, (x, y, 50, 50), 8)
game = True
while game:
    screen.blit(area, (500, 100))
    screen.blit(snake, (875, 375))
    screen.blit(apple, (800, 400))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
        elif i.type == pygame.KEYDOWN:
                if i.key == pg.K_LEFT:
                    x -= 15
                elif i.key == pg.K_RIGHT:
                    x += 15
                elif i.key == pg.K_UP:
                    y -= 15
                elif i.key == pg.K_DOWN:
                    y += 15
    sc.fill((0,0,0))
    pygame.draw.rect(sc, PUR, (x, y, 50, 50), 8)



x = 100
y = 100
screen.blit(area, (300, 300))


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("SPACE"*20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("SPACE")

    pygame.display.update()
pygame.quit()


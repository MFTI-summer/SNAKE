import pygame as pg
import sys

#### from pygame.locals import * - чтобы меньше писать
import pygame.sprite

pg.init()

#МУЗЫКА
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("SOUNDS/musictest1.ogg")
mt = 1
pygame.mixer.music.play(loops=1)




def play_music():
    global mt
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.unload()
        print('mt', mt)
        if mt >= 3:
            mt = 0
        # mt%= 4

        mt += 1
        nm = f"SOUNDS/musictest{mt}.ogg"
        pygame.mixer.music.load(nm)
        pygame.mixer.music.play(loops=1)


### ЭКРАН
W = 1000  # ширина
H = 800  # высота
sc = pg.display.set_mode((W, H))  # длина высота окна

# FPS
FPS = 60
clock = pg.time.Clock()

# GAME OVER
font = pygame.font.Font(None, 20)
text = font.render("Game over!", True, (255, 0, 0))

# snake HEAD ГОЛОВА ЗМЕИ
# PUR = (100, 128, 255)  #ЦВЕТ ЗМЕИ
# head = pg.draw.rect(sc, PUR, (480, 350, 60, 60), 8)


# ЯБЛОКО
class Apple(pg.sprite.Sprite):

    image = pg.image.load("IMG/apple.png")

    def __init__(self):
        self.image = Apple.image
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 400


apple = Apple()


# ЗМЕЯ
class SnakeBody(pg.sprite.Sprite):

    head = pg.image.load("IMG/snake/head.png")
    body = pg.image.load("IMG/snake/body.png")
    trail = pg.image.load("IMG/snake/trail.png")


    def __init__(self, x, y):
        self.image = SnakeBody.body
        self.rect = self.image.get_rect(x = x, y = y)


snake = SnakeBody(480, 350)



speed_x = 0
speed_y = 0



game = True
while game:
    clock.tick(FPS)  # задержка

    #play_music()

    for i in pg.event.get():  # в пг из папки ивент фн гет, присваиает перем зн
        if i.type == pg.QUIT:
            game = False
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                speed_x = -5

            elif i.key == pg.K_RIGHT:
                speed_x = 5

            elif i.key == pg.K_UP:
                speed_y = -5
            elif i.key == pg.K_DOWN:
                speed_y = 5

    snake.rect.x += speed_x
    snake.rect.y += speed_y

    if apple.rect.colliderect(snake.rect):
        print(123)

    if snake.rect.top <= 0 or snake.rect.bottom >= H:
        textpos = (10, 10)
        screen.blit(text, textpos)

    if snake.rect.left <= 0 or snake.rect.right >= W:
        game = False





    sc.fill((0, 0, 0))

    sc.blit(apple.image, apple.rect)
    sc.blit(snake.image, snake.rect)


    pg.display.update()  # обновление экрана

pg.quit()

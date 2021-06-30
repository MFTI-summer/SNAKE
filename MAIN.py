import pygame as pg
import sys

#### from pygame.locals import * - чтобы меньше писать
import pygame.sprite
from random import randint

pg.init()

# МУЗЫКА
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("SOUNDS/music1.ogg")
mt = 0


def play_music():
    global mt
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.unload()
        print('mt', mt)
        if mt >= 3:
            mt = 0
        mt += 1
        nm = f"SOUNDS/music{mt}.ogg"
        pygame.mixer.music.load(nm)
        pygame.mixer.music.play(loops=1)


### ЭКРАН
W = 1000 # ширина
H = 800  # высота
SIZE = 20

sc = pg.display.set_mode((W, H))  # длина высота окна

# FPS
FPS = 60
clock = pg.time.Clock()


# ЯБЛОКО
class Apple(pg.sprite.Sprite):
    image = pg.image.load("_Maxim/Apple.png")

    ## TODO Изменить размер яблока на SIZE

    def __init__(self):
        self.image = Apple.image
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 400

    def change_pos(self):
        self.rect.x = randint(0, 1000)
        self.rect.y = randint(0, 800)



# ЗМЕЯ
class Snake(pg.sprite.Sprite):
    head = pg.image.load("IMG/snake/head.png")
    body = pg.image.load("IMG/snake/body.png")
    trail = pg.image.load("IMG/snake/trail.png")

    # TODO изменить размер всех трёх кусков змеи на SIZE

    block = pg.Surface((SIZE, SIZE))
    block.fill((0, 255, 0))

    def __init__(self, x, y):
        self.image = Snake.head
        self.rect = self.image.get_rect(x=x, y=y)

        self.body = [pg.Rect(x + SIZE, y, SIZE, SIZE), pg.Rect(x + SIZE * 2, y, SIZE, SIZE),
                     pg.Rect(x + SIZE * 3, y, SIZE, SIZE)]

        self.speed_x = 0
        self.speed_y = 0
        self.cooldown = pygame.time.get_ticks()
        self.isApple = False
        self.score = 0

    def update(self, events):
        for e in events:

            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    self.speed_x = -SIZE
                    self.speed_y = 0

                elif e.key == pg.K_RIGHT:
                    self.speed_x = SIZE
                    self.speed_y = 0

                elif e.key == pg.K_UP:
                    self.speed_y = -SIZE
                    self.speed_x = 0
                elif e.key == pg.K_DOWN:
                    self.speed_y = SIZE
                    self.speed_x = 0

        if pygame.time.get_ticks() - self.cooldown > 200 and (self.speed_x != 0 or self.speed_y != 0):

            self.body.insert(0, self.rect.copy())
            if self.isApple == False:
                self.body.pop()
                self.isApple = False

            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.cooldown = pygame.time.get_ticks()

    def eat_apple(self):
        ## TODO этот метод должен запускаться для змеи если она столкнулась с яблоком
        ## TODO Увеличить переменную self.score
        self.isApple = True

    def draw(self):
        sc.blit(Snake.block, self.rect)

        for block in self.body:
            sc.blit(Snake.block, block)

    def collide(self):
        self.rect.x = 400
        self.rect.y = 200
        self.speed_x = 0
        self.speed_y = 0

        ## обнуление счета



        # TODO Что должна делать змея при столкновении?
        # TODO  отбросить хвост, обнулить счёт
        pass


apple = Apple()
snake = Snake(400, 200)

game = True
while game:
    clock.tick(FPS)  # задержка

    play_music()

    events = pg.event.get()

    for i in events:  # в пг из папки ивент фн гет, присваиает перем зн
        if i.type == pg.QUIT:
            game = False

    snake.update(events)

    if apple.rect.colliderect(snake.rect): ## Проверка столкновения змеи с яблоком
        apple.change_pos()


        ## TODO Яблоко запускает метод change_pos, змея запускает метод eat_apple
        print("Змея сталкивается с яблоком")

    if snake.rect.top <= 0 or snake.rect.bottom >= H:
        snake.collide()
        #game = False

    if snake.rect.left <= 0 or snake.rect.right >= W:
        snake.collide()
        #game = False



    ## ОТРИСОВКА на экран
    sc.fill((0, 0, 0))
    sc.blit(apple.image, apple.rect)
    snake.draw()


    pg.display.update()  # обновление экрана

pg.quit()

import pygame as pg
import sys

#### from pygame.locals import * - чтобы меньше писать
import pygame.sprite



pg.init()

#МУЗЫКА
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
W = 1000  # ширина
H = 800  # высота
SIZE = 20
sc = pg.display.set_mode((W, H))  # длина высота окна





# FPS
FPS = 60
clock = pg.time.Clock()



# ЯБЛОКО
class Apple(pg.sprite.Sprite):

    image = pg.image.load("_Maxim/Apple.png")
    ## TODO Изменить размер яблока на 100х100

    def __init__(self):
        self.image = Apple.image
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 400

    ## TODO метод change_pos() кторый назначет x и y новые координаты


apple = Apple()


# ЗМЕЯ
class Snake(pg.sprite.Sprite):

    head = pg.image.load("IMG/snake/head.png")
    body = pg.image.load("IMG/snake/body.png")
    trail = pg.image.load("IMG/snake/trail.png")
    head = pg.transform.scale(head, (SIZE, SIZE))
    body = pg.transform.scale(body, (SIZE, SIZE))
    trail = pg.transform.scale(trail, (SIZE, SIZE))
    block = pg.Surface((SIZE, SIZE))
    block.fill((255,0,0))


    def __init__(self, x, y):
        self.image = Snake.head
        self.rect = self.image.get_rect(x = x, y = y)

        self.body = [pg.Rect(x+SIZE, y, SIZE, SIZE ), pg.Rect(x+SIZE*2, y, SIZE, SIZE ), pg.Rect(x+SIZE*3, y, SIZE, SIZE )]

        self.speed_x = 0
        self.speed_y = 0
        self.cooldown = pygame.time.get_ticks()


    def update(self, events):
        for e in events:
            print(e)
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

        if pygame.time.get_ticks() - self.cooldown > 400:

            self.body.insert(0, self.rect.copy())
            self.body.pop()

            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.cooldown = pygame.time.get_ticks()



    def draw(self):
        sc.blit(Snake.block, self.rect)

        for block in self.body:
            sc.blit(Snake.block, block)





snake = Snake(400, 200)




speed_x = 0
speed_y = 0



game = True
while game:
    clock.tick(FPS)  # задержка

    play_music()

    events = pg.event.get()

    for i in events:  # в пг из папки ивент фн гет, присваиает перем зн
        if i.type == pg.QUIT:
            game = False

    snake.update(events)



    if apple.rect.colliderect(snake.rect):
        print(123)

    if snake.rect.top <= 0 or snake.rect.bottom >= H:
        game = False

        ## TODO Змея должна вернуться в начало


    if snake.rect.left <= 0 or snake.rect.right >= W:
        game = False






    sc.fill((0, 0, 0))


    snake.draw()
    sc.blit(apple.image, apple.rect)
    # sc.blit(snake.image, snake.rect)


    pg.display.update()  # обновление экрана

pg.quit()

import pygame as pg
import pygame.sprite
from random import choice

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
        if mt >= 4:
            mt = 0
        mt += 1
        nm = f"SOUNDS/music{mt}.ogg"
        pygame.mixer.music.load(nm)
        pygame.mixer.music.play(loops=1)

### ЭКРАН
W = 1680  # ширина
H = 900  # высота
SIZE = 30 #Размер одной клетки\блока
APPLESIZE = 60
sc = pg.display.set_mode((W, H))  # длина высота окна
fon = pg.image.load("IMG/Fon.png")
fon = pg.transform.scale(fon, (W, H))
# FPS
FPS = 60
clock = pg.time.Clock()

#  SCORE AND LIVES
f1 = pg.font.Font(None, 50)  # выводит на экран надпись 'Score:'
text1 = f1.render(f'Score: {0}', True, (255, 255, 255))
text2 = f1.render(f'GAME OVER', True, "#00796B")
text3 = f1.render(f'Lives: {3}', True, (255, 255, 255))

# ЯБЛОКО
class Apple(pg.sprite.Sprite):
    image = pg.image.load("_Maxim/Apple.png")
    image = pg.transform.scale(image, (APPLESIZE, APPLESIZE))

    def __init__(self):
        self.image = Apple.image
        self.rect = self.image.get_rect(x = 200, y = 400)
        # self.rect.x = 200
        # self.rect.y = 400

    def change_pos(self):
        self.rect.x = choice(range(60, W-60, APPLESIZE))
        self.rect.y = choice(range(60, H-60, APPLESIZE))


# ЗМЕЯ
class Snake(pg.sprite.Sprite):
    head = pg.image.load("IMG/snake/head.png")
    body = pg.image.load("IMG/snake/body.png")
    trail = pg.image.load("IMG/snake/trail.png")

    head = pg.transform.scale(head, (SIZE, SIZE))
    body = pg.transform.scale(body, (SIZE, SIZE))
    trail = pg.transform.scale(trail, (SIZE, SIZE))
    block = pg.Surface((SIZE, SIZE))
    block.fill((255, 0, 0))

    block = pg.Surface((SIZE, SIZE))
    block.fill((10, 0, 60))


    COOLDOWN = 100



    def __init__(self, x, y):
        super().__init__()
        self.image = Snake.head
        self.rect = self.image.get_rect(x=x, y=y)

        self.body = [pg.Rect(x + SIZE, y, SIZE, SIZE), pg.Rect(x + SIZE * 2, y, SIZE, SIZE),
                     pg.Rect(x + SIZE * 3, y, SIZE, SIZE)]
        self.downlives = False
        self.speed_x = 0
        self.speed_y = 0
        self.cooldown = pygame.time.get_ticks()
        self.isApple = False
        self.score = 0
        self.lives = 3

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

        self.move()

    def move(self):

        # Проверяем, что прошло достаточно времени для движения
        if pygame.time.get_ticks() - self.cooldown > Snake.COOLDOWN and (self.speed_x != 0 or self.speed_y != 0):

            self.cooldown = pygame.time.get_ticks()
            #записываем старую позицию головы в туловище
            self.body.insert(0, self.rect.copy())

            # Если не съели яблоко, то удаляем конец хвоста
            if self.isApple == False:
                self.body.pop()
            else:
                self.isApple = False


            #Двигаемся по x
            self.rect.x += self.speed_x

            if self.rect.bottom <= 0: #если вышли за верхнюю границу экрана
                self.rect.bottom = H
            if self.rect.top >= H:#если вышли за нижнюю границу экрана
                self.rect.top = 0

            self.rect.y += self.speed_y
            if self.rect.left >= W: #если вышли за правую границу экрана
                self.rect.left = 0

            if self.rect.right <= 0:#если вышли за левую границу экрана
                self.rect.right = W

            self.chek_trail_collide()

    def chek_trail_collide(self):
        global text1
        global text3
        for i, block in enumerate(self.body):
            if block.colliderect(self.rect):
                self.body = self.body[:i]
                self.score = 0
                self.lives -= 1
                text1 = f1.render(f'Score: {self.score}', True, (255, 255, 255))
                text3 = f1.render(f'Lives: {self.lives}', True, (255, 255, 255))
                self.downlives = True
            self.downlives = False

    def eat_apple(self):
        global text1
        self.isApple = True
        self.score += 1
        text1 = f1.render(f'Score: {self.score}', True, (255, 255, 255))

    def draw(self):
        sc.blit(Snake.block, self.rect)

        for block in self.body:
            sc.blit(Snake.block, block)

    def collide(self):
        if self.rect.x == 1000:
            self.rect.x = 0
        elif self.rect.x == 0:
            self.rect.x = 1000

        if self.rect.y == 800:
            self.rect.y = 0
        elif self.rect.y == 0:
            self.rect.y = 800






##++++++===============+++=======================================================================================================
apple = Apple()
snake = Snake(400, 200)

def main():
    game = True
    while game:
        play_music()
        clock.tick(FPS)  # задержка

        events = pg.event.get()
        for i in events:  # в пг из папки ивент фн гет, присваиает перем зн
            if i.type == pg.QUIT:
                game = False

        snake.update(events)

        if apple.rect.colliderect(snake.rect):  ## Проверка столкновения змеи с яблоком
            apple.change_pos()
            snake.eat_apple()

        if snake.lives == 0:
            game = False






        ## ОТРИСОВКА на экран
        #sc.fill((0, 0, 0))
        sc.blit(fon, (0,0))
        sc.blit(text1, (800, 50))
        sc.blit(text3, (650, 50))
        sc.blit(apple.image, apple.rect)
        snake.draw()
        pg.display.update()  # обновление экрана

def end_game():
    game = True
    pygame.mixer.music.load("SOUNDS/music5.ogg")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=-1)
    while game:

        clock.tick(FPS)  # задержка

        events = pg.event.get()
        for i in events:  # в пг из папки ивент фн гет, присваиает перем зн
            if i.type == pg.QUIT:
                game = False

        sc.fill((0, 0, 0))
        sc.blit(text2, (100, 200))

        pg.display.update()  # обновление экрана


        sc.fill((0, 0, 0))
        sc.blit(text2, (800, 50))

main()
end_game()
pg.quit()

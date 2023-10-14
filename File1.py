# Робимо прості змінні
import pygame
from pygame import *
from random import randint
from random import choice

pygame.init()
mw = pygame.display.set_mode((500, 500))
back = (200, 255, 255)
mw.fill(back)
move_right = False
move_left = False
game_over = False
win_count = 0
clock = time.Clock()
coordinates = [90, 170, 250, 320]


# Тут тиримо класси з Арканоїда
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 500 - 100:
            self.rect.x += self.speed


class Snacks(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 450:
            lost += 1
            self.rect.y = 0
            self.rect.x = choice(coordinates)


# Створюємо Котика
pop_cat = Player("Pop_cat.png", 250, 75, 75, 75, 7)

#Створюємо рибок
snacks = sprite.Group()
for i in range(2):
    snack1 = Snacks("Fish1.png", choice(coordinates), -40, 80, 40, randint(1, 5))
    snack2 = Snacks("Fish2.png", choice(coordinates), -40, 80, 40, randint(1, 5))
    snacks.add(snack1)
    snacks.add(snack2)
#І кукумбер
cucumber("cucumber.png", choice(coordinates), -40, 80, 40, randint(1, 5))
# Далі йде ігровий код
score = 0
lost = 0
while not game_over:
    mw.blit(back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    if move_right:
        pop_cat.rect.x += 3
    if move_left:
        pop_cat.rect.x -= 3

    for e in event.get():
        if e.type == QUIT:
            run = False
    collision = sprite.spritecollide(pop_cat, snacks, True)
    for c in collision:
        score += 1
        snack = Snacks("scooby-snack44.png", choice(coordinates), -40, 80, 40, randint(1, 3))
        snacks.add(snack)

    text1 = font.render("Пропущено : " + str(lost), True, (255, 255, 255))
    mw.blit(text1, (10, 60))
    text2 = font.render("Зловлено : " + str(score), True, (255, 255, 255))
    mw.blit(text2, (10, 20))

    snacks.draw(mw)
    snacks.update()
    pop_cat.reset()
    pop_cat.update()

    if win_count == 5:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('YOU WIN', 60, (0, 200, 0))
        time_text.draw(10, 10)
        game_over = True

# Далі нудне, рух всіх об'єктів, кроме котика

    if snack1.rect.y == -1:
        snack1.rect.y = (randint(1, 500))

    if snack2.rect.y == -1:
        snack2.rect.y = (randint(1, 500))

    if Cucumber1.rect.y == -1:
        Cucumber1.rect.y = (randint(1, 500))

        pygame.display.update()
        clock.tick(40)
#Робимо прості змінні
import pygame
import random
pygame.init()
mw = pygame.display.set_mode((500, 500))
back = (200, 255, 255)
mw.fill(back)
move_right = False
move_left = False
game_over = False
win_count = 0


#Тут тиримо класси з Арканоїда
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.drawt.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def drawt(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def drawt(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

#Створюємо Котика
Pop_cat = Picture("D:\Картинки для Пайтона\Pop_cat.png", 250, 75, 75, 75  )
Pop_cat = pygame.transform.scale(Pop_cat, (75, 75))
#Створюємо перших рибок
Fish1 = Picture("D:\Картинки для Пайтона\Fish1.png", 100, 350, 25, 25 )
Fish1 = pygame.transform.scale(Fish1, (75, 70))
Fish2 = Picture("D:\Картинки для Пайтона\Fish1.png", 100, 350, 25, 25 )
Fish2 = pygame.transform.scale(Fish1, (75, 70))
#Створюємо Других рибок
Fish3 = Picture("D:\Картинки для Пайтона\Fish1.png", 100, 350, 25, 25 )
Fish3 = pygame.transform.scale(Fish1, (75, 70))
Fish4 = Picture("D:\Картинки для Пайтона\Fish1.png", 100, 350, 25, 25 )
Fish4 = pygame.transform.scale(Fish1, (75, 70))
#Створюємо Огірочок
Cucumber1 = Picture("D:\Картинки для Пайтона\Cucumber.png", 300, 350, 25, 25)
Cucumber1 = pygame.transform.scale(Cucumber, (75, 70))
Cucumber2 = Picture("D:\Картинки для Пайтона\Cucumber.png", 300, 350, 25, 25)
Cucumber2 = pygame.transform.scale(Cucumber, (75, 70))
#Далі йде ігровий код

while not game_over: 
    Pop_cat.fill()
    Pop_cat.drawt()
    Cucumber1.fill()
    Cucumber2.fill()
    Cucumber1.drawt()
    Cucumber2.drawt()
    Fish1.drawt()
    Fish1.fill()
    Fish2.fill()
    Fish2.drawt()
    Fish3.fill()
    Fish3.drawt()
    Fish4.fill()
    Fish4.drawt()
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
      Pop_cat.rect.x +=3 
    if move_left: 
      Pop_cat.rect.x -=3 

    if Pop_cat.rect.colliderect(Fish1) or (Fish2) or (Fish3) or (Fish4):
        win_count += 1

    if Pop_cat.rect.colliderect(Cucumber1) or (Cucumber2):
        time_text = Label(150,150,50,50,back) 
        time_text.set_text('YOU LOSE',60, (255,0,0)) 
        time_text.drawt(10, 10) 
        game_over = True

    if win_count == 5:
        time_text = Label(150,150,50,50,back) 
        time_text.set_text('YOU WIN',60, (0,200,0)) 
        time_text.drawt(10, 10) 
        game_over = True

#Далі нудне, рух всіх об'єктів, кроме котика

    if Fish1.rect.y == -1:
        Fish1.rect.y = (randint(1, 500))

    if Fish2.rect.y == -1:
        Fish2.rect.y = (randint(1, 500))

    if Fish3.rect.y == -1:
        Fish3.rect.y = (randint(1, 500))

    if Fish4.rect.y == -1:
        Fish4.rect.y = (randint(1, 500))
    
    if Cucumber1.rect.y == -1:
        Cucumber1.rect.y = (randint(1, 500))
    
    if Cucumber2.rect.y == -1:
        Cucumber2.rect.y = (randint(1, 500))




        pygame.display.update() 
        clock.tick(40)
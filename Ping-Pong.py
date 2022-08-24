from pygame import *
from random import randint
from time import time as timer
win = display.set_mode((800, 500))
background = transform.scale(image.load('fon.jpg'), (800, 500))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont(None, 40)
lost = 0
kills = 0
pictures = ['object1.png', 'object2.png', 'object3.png', 'object4.png']

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

racket1 = Player('racket.png', 5, 200, 50, 150, 7)
racket2 = Player('racket.png', 750, 200, 50, 150, 7)
ball = GameSprite('krug.png', 200, 200, 50, 50, 5)
speed_x = 3
speed_y = 3

winner1 = font1.render('Player 1 WIN!', True, (0, 255, 0))
winner2 = font1.render('Player 2 WIN!', True, (0, 255, 0))
game = True
finish = False
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        win.blit(background, (0, 0))
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            win.blit(winner2, (350, 250))
        if ball.rect.x > 880:
            finish = True
            win.blit(winner1, (350, 250))


    display.update()
    clock.tick()

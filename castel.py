#Создай собственный Шутер!
from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, player_x, player_y, speed_x, speed_y, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (wight, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        key_pressed = key.get_pressed()
        
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if key_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 15, 20)
        bullets.add(bullet)
        fire.play()
        

class Enemy(GameSprite):

    def update(self):
        global lost
        global live

        self.rect.y += self.speed

        if self.rect.y >= 500:
            
            self.rect.x = randint(80, 620)
            self.rect.y = 0
            self.speed = randint(1, 3)

            lost += 1 

            if lost % 3 == 0:
                live -= 1
    
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
          
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
    
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Asteroids(GameSprite):
    def update(self):
        global lost

        self.rect.y += self.speed

        if self.rect.y >= 500:
            
            self.rect.x = randint(80, 620)
            self.rect.y = 0
            self.speed = randint(1, 3)
 
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption('Castel')

background = transform.scale(image.load('background.png'), (700,500))

font.init()
font1 = font.Font(None, 30)
font2 = font.Font(None, 70)
win = font2.render('YOU WIN!', True, (255, 215, 0))
lose = font2.render('YOU LOSE!', True, (255, 0, 0))

mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()

#fire = mixer.Sound('fire.ogg')
clock = time.Clock()

#player = Player('player.png', 325, 410, 10, 90, 90)

run = True
finish = False

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.y += speed_y
                
            
   #if finish != True: 
   #    window.blit(background,(0, 0))

   #    player.reset()
   #    player.update()
    window.blit(background,(0, 0))
    clock.tick(40)
    display.update()

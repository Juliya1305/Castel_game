from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, player_x, player_y, speed_x, speed_y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect_bottom = 0
        self.rect= self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = width
        self.height = height
        self.speed_x = speed_x
        self.speed_y = speed_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def jump(self, make_jump, jump_counter):
        
        if jump_counter >= -30:
            self.rect.y -= jump_counter // 3
            jump_counter -= 1
   
        else:
            jump_counter = 30
            make_jump = False
        
        return make_jump, jump_counter
    
    def update(self):
        dx = 0
        dy = 0
        #jumpCount = 0
        #isJump = False
        Down = True

        make_jump = False
        jump_counter = 30
        

        key_pressed = key.get_pressed()
        
        if key_pressed[K_LEFT] and self.rect.x > 0:
            dx -= self.speed_x
            self.image = transform.scale(image.load('knight_l.png'), (90, 90))

        if key_pressed[K_RIGHT] and self.rect.x < 640:
            dx += self.speed_x
            self.image = transform.scale(image.load('knight_r.png'), (80, 80))

        if key_pressed[K_UP]:  #and isJump == False :
            #jumpCount = -10
            make_jump = True
        
        if make_jump:
           make_jump, jump_counter = player.jump(make_jump, jump_counter)

        #if key_pressed[K_UP] == False :
        #    isJump = False
        
        #jumpCount += 1
        #if jumpCount > 10:
        #    jumpCount = 10

        

        if  (-10 < self.rect.x < 180) and (50 < self.rect.y < 60):
            Down = False

        if (450 < self.rect.x < 700) and (50 < self.rect.y < 60):
            Down = False
        
        if  (160 < self.rect.x < 380) and (170 < self.rect.y < 180):
            Down = False
        
        if  (70 < self.rect.x < 190) and (300 < self.rect.y < 310):
            Down = False

        if  (450 < self.rect.x < 600) and (300 < self.rect.y < 310):
            Down = False

        if  (-10 < self.rect.x < 100) and (410 < self.rect.y < 420):
            Down = False

        if  (140 < self.rect.x < 380) and (410 < self.rect.y < 420):
            Down = False
        
        if  (550 < self.rect.x < 700) and (410 < self.rect.y < 420):
            Down = False

        #dy += jumpCount
        dy += jump_counter
        self.rect.x += dx
        if Down:
            self.rect.y += dy

        if self.rect.bottom > 650:
           self.rect.bottom = 650
           dy = 0 
    
    
    

class World():
    def __init__(self, data):
        
        self.tile_list = []
        
        plathorm_img = image.load('platforma.png')
        row_count =  0
        
        for row in data:
            col_count = - 150
            for tile in row:
                if tile == 1:
                    img = transform.scale(plathorm_img, (tile_size_x, tile_size_y))
                    img_rect = img.get_rect() 
                    img_rect.x = col_count + 150
                    img_rect.y = row_count + 100
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    

                col_count += 100
            row_count += 125

    def draw(self):
        for tile in self.tile_list:
            window.blit(tile[0], tile[1])




window = display.set_mode((700, 650))
display.set_caption('Castel')

tile_size_x = 125
tile_size_y = 100

background = transform.scale(image.load('background.png'), (700, 650))

font.init()
font1 = font.Font(None, 30)
font2 = font.Font(None, 70)
win = font2.render('YOU WIN!', True, (255, 215, 0))
lose = font2.render('YOU LOSE!', True, (255, 0, 0))

count_keys = 0
count = font1.render('Ключи: ' + str(count_keys), True, (255, 215, 0))


mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()

#fire = mixer.Sound('fire.ogg')
clock = time.Clock()

player = Player('knight_r.png', 20, 500, 10, 10, 80, 80)
princess = GameSprite('princess.png', 600, 25, 0, 0, 100, 100)
prison = GameSprite('prison.png', 605, 25, 0, 0, 100, 100)
key1 = GameSprite('key.png',25, 25, 0, 0, 100, 100)
key2 = GameSprite('key.png',100, 300, 0, 0, 100, 100)
key3 = GameSprite('key.png',600, 400, 0, 0, 100, 100)

world_data = [
[1, 1, 0, 0, 0, 1, 1],
[0, 0, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 1, 0],
[1, 0, 1, 1, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0],
 ] 

world = World(world_data)

keys = sprite.Group()
keys.add(key1)
keys.add(key2)
keys.add(key3)



run = True
finish = False

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
     
    if finish != True: 
        window.blit(background,(0, 0))

        
        world.draw()
        keys.draw(window)

        player.reset()
        princess.reset()
        prison.reset()
        keys.update()

        player.update()

        sprites_list = sprite.spritecollide(player, keys, True)

    clock.tick(120)
    display.update() 
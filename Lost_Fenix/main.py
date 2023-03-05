import random
import time
import pygame

pygame.init()
pygame.mixer.init()

class Settings:
    music_active = True
    shoot_sound = None
    boom_sound = None
    game_active = False

    @classmethod
    def load_n_play_music(cls,path_to_music):
        pygame.mixer.music.load(path_to_music)
        pygame.mixer.music.play()

    @classmethod
    def set_volume(cls,volume):
        pygame.mixer.music.set_volume(volume)

    @classmethod
    def pause_unpause_music(cls):
        if Settings.music_active == True:
            pygame.mixer.music.pause()
            Settings.music_active = False
        else:
            pygame.mixer.music.unpause()
            Settings.music_active = True
    @classmethod
    def load_shoot_sound(cls, path_to_sound):
        Settings.shoot_sound = pygame.mixer.Sound(path_to_sound)

    @classmethod
    def set_shoot_volume(cls, volume):
        Settings.shoot_sound.set_volume(volume)

    @classmethod
    def play_shoot_sound(cls):
        Settings.shoot_sound.play()

    @classmethod
    def load_boom_sound(cls, path_to_sound):
        Settings.boom_sound = pygame.mixer.Sound(path_to_sound)

    @classmethod
    def set_boom_volume(cls, volume):
        Settings.boom_sound.set_volume(volume)

    @classmethod
    def play_boom_sound(cls):
        Settings.boom_sound.play()

def main_menu():
    Settings.game_active = False
    fm = pygame.font.Font(None, 100)
    click = False
    mx = 0
    my = 0
    while Settings.game_active == False:
        display.fill(Black)
        display.blit(background_im,(0,0))

        quit = fm.render('Quit?',True,White)
        play = fm.render('Escape!',True,White)
        settings = fm.render('Sound settings', True, White)
        title = fq.render('Lost Ship', True, White)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEMOTION:
                mx = event.pos[0]
                my = event.pos[1]
                print(mx,my)
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
            if click == True:
                if mx >= 100 and mx <= 430 and my <= 480 and my >= 400:
                    Settings.game_active = True
                if mx >= 100 and mx <= 300 and my <= 680 and my >= 600:
                    pygame.quit()
                if mx >= 100  and mx <= 620 and my <= 580  and my >= 500:
                    call_settings()
        if mx >= 100 and mx <= 430 and my <= 480 and my >= 400:
            pygame.draw.rect(display, Green, (100, 400, 275, 80))
        else:
            pygame.draw.rect(display, Black, (100, 400, 275, 80))

        if mx >= 100 and mx <= 300 and my <= 680 and my >= 600:
            pygame.draw.rect(display, Red, (100, 600, 200, 80))
        else:
            pygame.draw.rect(display, Black, (100, 600, 200, 80))

        if mx >= 100  and mx <= 1200 and my <= 250 and my >= 100:
            pygame.draw.rect(display, Yellow, (100, 100, 1200, 250))
        else:
            pygame.draw.rect(display, Black, (100, 100, 1200, 250))

        if mx >= 100  and mx <= 620 and my <= 580  and my >= 500:
            pygame.draw.rect(display, Purple, (100, 500, 520, 80))
        else:
            pygame.draw.rect(display, Black, (100, 500, 520, 80))
    
        display.blit(settings,(100,500))
        display.blit(quit,(100,600))
        display.blit(play, (100, 400))
        display.blit(title, (100, 100))

        pygame.display.update()

def call_settings():
    Settings.game_active = False
    fm = pygame.font.Font(None, 100)
    f2 = pygame.font.Font(None, 250)
    setted_sound_volume = 0.3
    click = False
    checked = False
    up = False
    down = False
    selected = 'None'
    mx = 0
    my = 0
    while Settings.game_active == False:
        display.fill(Black)
        display.blit(background_im, (0, 0))

        quit = fm.render('Quit?', True, White)
        volume = fm.render('Set volume:', True, White)
        title = f2.render('Sound settings', True, White)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_LEFT and selected == 'SetVolume':
                    down = True
                if event.key == pygame.K_RIGHT and selected == 'SetVolume':
                    up = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    up = False
                if event.key == pygame.K_LEFT:
                    down = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEMOTION:
                mx = event.pos[0]
                my = event.pos[1]
                print(mx, my)
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
            if click == True:
                if mx >= 100 and mx <= 485 and my <= 480 and my >= 400 and selected == 'None'and checked == False:
                    selected = 'SetVolume'
                    checked = True
                if mx >= 100 and mx <= 485 and my <= 480 and my >= 400 and selected == 'SetVolume' and checked == False:
                    selected = 'None'
                    checked = True
                if mx >= 100 and mx <= 300 and my <= 680 and my >= 600:
                    main_menu()
        if up == True and setted_sound_volume <= 1:
            setted_sound_volume += 0.01
        if down == True and setted_sound_volume >= 0:
            setted_sound_volume -= 0.01
        if selected == 'SetVolume':
            pygame.draw.rect(display, Purple, (100, 400, 388, 80))
        else:
            pygame.draw.rect(display, Black, (100, 400, 388, 80))

        if mx >= 100 and mx <= 300 and my <= 680 and my >= 600:
            pygame.draw.rect(display, Red, (100, 600, 200, 80))
        else:
            pygame.draw.rect(display, Black, (100, 600, 200, 80))

        if mx >= 100 and mx <= 1200 and my <= 250 and my >= 100:
            pygame.draw.rect(display, Yellow, (100, 100, 1280, 210))
        else:
            pygame.draw.rect(display, Black, (100, 100, 1280, 210))


        display.blit(quit, (100, 600))
        display.blit(volume, (100, 400))
        display.blit(title, (100, 100))
        pygame.draw.rect(display,Purple,(100, 500, setted_sound_volume * 500, 40))

        Settings.set_volume(setted_sound_volume/1.5)
        Settings.set_shoot_volume(setted_sound_volume)
        Settings.set_boom_volume(setted_sound_volume)

        pygame.display.update()
        checked = False

class GameObject:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.size = 40
        self.speed = 20.0
        self.color = Black
        self.has_image = False
        self.image = None

    def draw(self):
        if self.has_image == False:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))
        if self.has_image:
            display.blit(self.image,(self.x,self.y))
    def add_image(self,path_to_image):
        im = pygame.image.load(path_to_image)
        self.image = pygame.transform.scale(im, (self.size,self.size))
        self.has_image = True
    def rotate_image(self, image, angle):
        self.image = pygame.transform.rotate(image,angle=angle)

class Boss(GameObject):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.color = Red
        self.pattern_x = 1
        self.speed = 10
        self.size = 60
    def move(self):
        self.x -= self.speed // 1.5 * self.pattern_x
        if self.x + self.size >= WIDTH:
            self.pattern_x = 1
        if self.x <= 0:
            self.pattern_x = -1
    def shoot(self, bullets):
        bullet = Projectile(self.x + self.size / 2 - 15,self.y,display,-1)
        bullet.add_image('kaboom.png')
        bullet.rotate_image(bullet.image,180)
        bullets.append(bullet)

class Enemy(GameObject):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.color = Red
        self.pattern_x = 1
        self.start_x = x
        self.speed = 5
    def move(self):
        self.x -= self.speed // 1.5 * self.pattern_x
        if self.x <= self.start_x - 80:
            self.y += self.speed
            self.pattern_x = -1
            self.speed += 0.5
        if self.x >= self.start_x + 120:
            self.y += self.speed
            self.pattern_x = 1
            self.speed += 0.5

class Hero(GameObject):
    def __init__(self, x, y,screen):
        super().__init__(x, y, screen)
        self.color = Green
        self.reload_time = 0.3 * FPS
    def move_rigth(self):
        if self.x + self.size + self.speed <= WIDTH:
            self.x += self.speed
    def move_left(self):
        if self.x - self.speed >= 0:
            self.x -= self.speed
    def shoot(self, bullets):
        bullet = Projectile(self.x + self.size / 2 - 15,self.y,display,1)
        bullet.add_image('kaboom.png')
        bullets.append(bullet)

class Boom(GameObject):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.color = Red
        self.size = 4
    def expand(self, b_list):
        self.size += 16
        self.x -= 8
        self.y -= 8
        if self.size >= 80:
            b_list.remove(self)

class Projectile(GameObject):
    def __init__(self, x, y, screen, align):
        super().__init__(x, y, screen)
        self.size = 30
        self.speed = 30
        self.color = Aqua
        self.align = align
        self.exist = True
    def move(self):
        self.y -= self.speed * self.align
    def check_colisions(self, enemy_list, boom_list,bosses_list,hero,bullets):
        if self.align == 1:
            for en in enemy_list:
                self.check(en,boom_list, enemy_list)
            for bos in bosses_list:
                self.check(bos,boom_list,bosses_list)
        else:
            if (self.x <= hero.x + hero.size and self.y <= hero.y + hero.size and self.x >= hero.x and self.y >= hero.y) or (
                    self.x + self.size <= hero.x + hero.size and self.y <= hero.y + hero.size and self.x + self.size >= hero.x and self.y >= hero.y):
                Settings.game_active = False
            if self.y >= HEIGHT:
                bullets.remove(self)
    def check(self,b, b_list, enemy_list):
        if (self.x <= b.x + b.size and self.y <= b.y + b.size and self.x >= b.x and self.y >= b.y) or (
                self.x + self.size <= b.x + b.size and self.y <= b.y + b.size and self.x + self.size >= b.x and self.y >= b.y):
            b_list.append(Boom(self.x, self.y, self.screen))
            enemy_list.remove(b)
            Settings.play_boom_sound()
            self.exist = False


WIDTH = 1440
HEIGHT = 1080

Black = (0,0,0)
White =(255,255,255)
Green = (0,255,0)
Blue = (0,0,255)
Red = (255,0,0)
Yellow = (175,205,0)
Aqua = (0,255,255)
Purple = (155,0,155)

display = pygame.display.set_mode((WIDTH,HEIGHT))

score = 0
FPS = 30
clock = pygame.time.Clock()
start_tick_shoot_boss = pygame.time.get_ticks()
f = pygame.font.Font(None,50)
fq = pygame.font.Font(None,350)

background_im = pygame.image.load('qasar.jpg')
background_im = pygame.transform.scale(background_im,(WIDTH,HEIGHT))


enemies = []
bullets = []
booms = []
bosses = []

boss = Boss(WIDTH/2 - 30,10,display)
boss.add_image('baka.png')
bosses.append(boss)


for i in range(16): #16
    for s in range(5): #5
        enemy = Enemy(80 + i*80,40 + s*80,display)
        enemy.add_image('baka.png')
        enemies.append(enemy)

hero = Hero(700,1000,display)
hero.add_image('fenix.png')
print(enemies)
iskeyd = False
iskeya = False
iskeyspace = False

Settings.load_n_play_music('music\\music.mp3')
Settings.set_volume(0.2)
Settings.load_shoot_sound('music\\laser.wav')
Settings.set_shoot_volume(0.3)
Settings.load_boom_sound('music\\boommusic.wav')
Settings.set_boom_volume(0.3)

main_menu()
while Settings.game_active:
    display.fill(Black)
    display.blit(background_im,(0,0))

    hero.reload_time -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                iskeyd = True
            if event.key == pygame.K_a:
                iskeya = True
            if event.key == pygame.K_p:
                Settings.pause_unpause_music()
            if event.key == pygame.K_SPACE:
                iskeyspace = True
            if event.key == pygame.K_ESCAPE:
                if Settings.game_active == True:
                    main_menu()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                iskeyd = False
            if event.key == pygame.K_a:
                iskeya = False
            if event.key == pygame.K_SPACE:
                iskeyspace = False

    if iskeya == True:
        hero.move_left()
    if iskeyd == True:
        hero.move_rigth()
    if iskeyspace == True:
        if hero.reload_time <= 0:
            hero.shoot(bullets)
            hero.reload_time = 0.3 *FPS
            Settings.play_shoot_sound()
    for v in enemies:
        v.move()
        v.draw()
        if v.y >= HEIGHT:
            Settings.game_active = False
    second_from_last_shoot_boss = (pygame.time.get_ticks() - start_tick_shoot_boss) / 1000

    for n in bosses:
        n.move()
        n.draw()
        if second_from_last_shoot_boss > random.random() * 10:
            n.shoot(bullets)
            start_tick_shoot_boss = pygame.time.get_ticks()

    for bullet in bullets:
        bullet.move()
        bullet.draw()
        bullet.check_colisions(enemies,booms,bosses,hero,bullets)
        if bullet.exist == False:
            bullets.remove(bullet)
            score += 1
    text = f.render(str(score),True, White)
    display.blit(text,(1,1))

    for boom in booms:
        boom.draw()
        boom.expand(booms)
    hero.draw()
    if len(enemies) == 0:
        win = fq.render('You Win:)',True, White)
        display.fill(Green)
        display.blit(win,(100,200))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
    pygame.display.update()
    clock.tick(FPS)

fqtext = fq.render('Game Over:<', True,White)
display.fill(Black)
display.blit(fqtext,(0,250))
pygame.display.update()
time.sleep(2)
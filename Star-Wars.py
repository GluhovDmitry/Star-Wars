import pygame 
import random
import os


width = 800
height = 400
fps = 60


pygame.init() #load game
pygame.mixer.init() #for sound

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Star Wars v 1.0")
clock = pygame.time.Clock() # frames
#colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#create an event for shooting

SHOOTINGEVENT = pygame.USEREVENT + 1

#folder for resources
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'resources/img')
player_img = pygame.image.load(os.path.join(img_folder, 'yoda.png'))
player_img_in_action = pygame.image.load(os.path.join(img_folder, 'yodaFight.png'))
opponent_img = pygame.image.load(os.path.join(img_folder, 'opponent.png'))
bolt_img = pygame.image.load(os.path.join(img_folder, 'bolt.png'))
#create an object 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (30, int(height/2))
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        mousestate = pygame.mouse.get_pressed()
        if keystate[pygame.K_d] and self.rect.right < width:
            self.speedx = 3
        if keystate[pygame.K_a] and self.rect.left > 0:
            self.speedx = -3
        if mousestate[0] == 1:
            self.image = player_img_in_action
        if mousestate[0] == 0:
            self.image = player_img
        self.rect.x += self.speedx
#mobs class
class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = opponent_img
        self.rect = self.image.get_rect()
        self.rect.center = (width - 30, int(height/2)-20)
    def update(self):
        self.speedx = 0
        self.rect.x += self.speedx
    def shoot(self):
        bullet = Bullet(self.rect.left, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
#bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bolt_img
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = -1
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x < 0:
            self.kill()
#add group of sprites
clock = pygame.time.Clock()
#groups of sprites
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
players = pygame.sprite.Group()
opponents = pygame.sprite.Group()
#instance of class Player
player = Player()
players.add(player)
#add player to group of sprites
all_sprites.add(player)
#group of mobs
for i in range(3):
    o = Opponent()
    all_sprites.add(o)
    opponents.add(o)
#periodic shooting
pygame.time.set_timer(SHOOTINGEVENT, 4000)
#game cycle
running = True
while running:
    #FPS controlling
    clock.tick(fps)

    #the list of events 
    for event in pygame.event.get():
        #check for closing
        if event.type == pygame.QUIT:
            running = False
        if event.type == SHOOTINGEVENT:
            for o in opponents:
                o.shoot()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for p in players:
                hits = pygame.sprite.spritecollide(p, opponents, True)
            bullet_hits = pygame.sprite.groupcollide(players, bullets, False, False)
            for bullet in bullet_hits:
                bullet.speedx = bullet.speedx*(-1)
        else: bullet_hits = pygame.sprite.groupcollide(players, bullets, True, True)

                
    #update sprites
    all_sprites.update()
    
    #render
    screen.fill(blue)
    #show sprites
    all_sprites.draw(screen)
    #after render - flip of the screen (optimising)
    pygame.display.flip()
pygame.quit()
import pygame 
import random
import os
from player import *
from opponent import *
from bullet import *
from variables import *


fps = 60

pygame.init() #load game
pygame.mixer.init() #for sound

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Star Wars v 1.0")
clock = pygame.time.Clock() # frames


#create an event for shooting

SHOOTINGEVENT = pygame.USEREVENT + 1


back_img = pygame.image.load(os.path.join(img_folder, 'background2.jpg'))
back_rect = back_img.get_rect()
#add group of sprites
clock = pygame.time.Clock()

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
kill = True
running = True
while running:
    #FPS controlling
    clock.tick(fps)
    #the list of events 
    for event in pygame.event.get():
        #check for closing
        if event.type == pygame.QUIT:
            running = False
        if event.type == SHOOTINGEVENT: #periodic shooting
            for o in opponents:
                o.shoot()
        if event.type == pygame.MOUSEBUTTONDOWN: #do not kill player when mouse down and kill opponent
            if event.button == 1:
                for p in players:
                    hits = pygame.sprite.spritecollide(p, opponents, True) #
                kill = False
        elif event.type == pygame.MOUSEBUTTONUP: #kill when mouse upped
             if event.button == 1:
                kill = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            player.up = True
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            player.up = False
    #update sprites
    all_sprites.update()
    bullet_hits = pygame.sprite.groupcollide(bullets, players, kill, kill)
    if not kill:
        for bullet in bullet_hits:
            bullet.speedx = bullet.speedx*(-1)
    #render
    screen.fill(blue)
    screen.blit(back_img, back_rect)
    #show sprites
    all_sprites.draw(screen)
    #after render - flip of the screen (optimising)
    pygame.display.flip()
pygame.quit()
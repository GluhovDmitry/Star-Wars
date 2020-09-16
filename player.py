import pygame 
import random
import os
from variables import *


a = 5 #acceleration
g = 0.2 #gravity

player_img = pygame.image.load(os.path.join(img_folder, 'yoda.png'))
player_img_in_action = pygame.image.load(os.path.join(img_folder, 'yodaFight.png'))

#create an object 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (30, int(height/2))
        self.onGround = True
        self.speedy = 0
        self.up = False
        self.rotationSpeed = 5
        self.rotation = 0
        self.last_update = pygame.time.get_ticks()
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
 
        if self.rect.center[1] >= int(height/2):
            self.onGround = True
        else: self.onGround = False

        if self.up:
            if self.onGround:
                self.speedy = -a
                
        elif not self.onGround:
            #self.rotate() 
            self.speedy += g
        elif self.onGround:
            self.speedy = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 15:
            self.last_update = now
            self.rotation = (self.rotation + self.rotationSpeed) % 360
            self.image = pygame.transform.rotate(self.image, self.rotation)
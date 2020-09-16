import pygame 
import random
import os
from bullet import *
from variables import *
from grass import *

opponent_img = pygame.image.load(os.path.join(img_folder, 'opponent.png'))
#mobs class
class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = opponent_img
        self.rect = self.image.get_rect()
        self.rect.center = (width - 300, int(height/2))
        self.speedy = 1
    def update(self):
        self.speedx = 0
        self.rect.x += self.speedx
        self.isOnGround()
        self.onGround = False
        self.rect.y += self.speedy
    def shoot(self):
        bullet = Bullet(self.rect.left, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def isOnGround(self):
        #if self.rect.center[1] >= int(height/2):
            #self.onGround = True
        #else: self.onGround = False
        for block in grassBlocks:
            if pygame.sprite.collide_rect(self, block):
                if self.speedy > 0:
                    self.rect.bottom = block.rect.top 
                    self.onGround = True 
                    self.speedy = 0
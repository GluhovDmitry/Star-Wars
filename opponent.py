import pygame 
import random
import os
from bullet import *
from variables import *

opponent_img = pygame.image.load(os.path.join(img_folder, 'opponent.png'))
#mobs class
class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = opponent_img
        self.rect = self.image.get_rect()
        self.rect.center = (width - 300, int(height/2))
    def update(self):
        self.speedx = 0
        self.rect.x += self.speedx
    def shoot(self):
        bullet = Bullet(self.rect.left, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
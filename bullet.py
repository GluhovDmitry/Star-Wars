import pygame 
import random
import os
from variables import *

bolt_img = pygame.image.load(os.path.join(img_folder, 'bolt.png'))

#bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bolt_img
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = -5
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x < 0:
            self.kill()
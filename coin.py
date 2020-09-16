import pygame 
import random
import os
from variables import *

coin_img = pygame.image.load(os.path.join(img_folder, 'coin.png'))

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = coin_img
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
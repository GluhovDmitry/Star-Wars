import pygame 
import random
import os
from variables import *
ironBlock_img = pygame.image.load(os.path.join(img_folder, 'metaltexture.jpg'))
#class of grass and blocks on level
class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        self.image = ironBlock_img
        #self.image.fill(black)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

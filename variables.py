import pygame 
import random
import os
#groups of sprites
players = pygame.sprite.Group()
opponents = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

width = 800
height = 400

#colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#folder for resources
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'resources/img')
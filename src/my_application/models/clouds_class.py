import pygame
import config
import textures
import random

class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = textures.CLOUD_IMG
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(config.SCREEN_WIDTH + 100, random.randint(50, 1030)))
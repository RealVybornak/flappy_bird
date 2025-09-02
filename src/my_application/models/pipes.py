import pygame
import config
import textures
import random

class Obsticles_Lower(pygame.sprite.Sprite):
    def __init__(self):
        global size
        super().__init__()
        size = random.randint(695,1365)
        self.surf = textures.LOWER_PIPE_IMG
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(config.SCREEN_WIDTH + 100, size)
        )


    def update(self):
        self.rect.move_ip(-config.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Obsticles_Upper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = textures.UPPER_PIPE_IMG
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(config.SCREEN_WIDTH + 100, (size - 780-250))
        )

    def update(self):
        self.rect.move_ip(-config.speed, 0)
        if self.rect.right < 0:
            self.kill()
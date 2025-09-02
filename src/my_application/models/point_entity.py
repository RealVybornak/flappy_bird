import pygame
import config

class Points(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, config.SCREEN_HEIGHT))
        self.surf.fill((135, 0, 250))
        self.rect = self.surf.get_rect(center=(config.SCREEN_WIDTH + 100, config.SCREEN_HEIGHT/2))

    def update(self):
        self.rect.move_ip(-config.speed, 0)
        if self.rect.right < 0:
            self.kill()
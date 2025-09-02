import pygame
import textures

pygame.init()

class Start(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = textures.START_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(1320, 750)
        )

class Quit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = textures.QUIT_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(600, 750)
        )

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = textures.MENU_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(1320, 750)
        )

class Retry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = textures.RETRY_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(600, 750)
        )


class Title(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = textures.TITLE_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(990,300)
        )

class Dummy_bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = textures.DUMMY_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(960,435)
        )
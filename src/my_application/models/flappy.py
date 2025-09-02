import pygame
import textures
import config
from pygame.locals import K_SPACE

import sys
sys.path.insert(1, 'C://Users//PC//OneDrive//Plocha//learning_python//flappy_bird//src//my_application//views')
import sound_manager

sounds = sound_manager.Sound_manager()
sounds.load_sound("wing_flap.mp3","assets/sounds")

class Player(pygame.sprite.Sprite):
    global VELOCITY
    VELOCITY = 1
    def __init__(self):
        super().__init__()
        self.surf = textures.PLAYER_IMG
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(center=(config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2))

    def movement(self, pressd_keys):
        global VELOCITY
        if pressd_keys[K_SPACE]:
            sounds.play_sound("wing_flap")
            if VELOCITY > 0:
                VELOCITY = 0
            if self.rect.top == 0:
                VELOCITY = -10    
            self.rect.move_ip(0, -10 + VELOCITY)
            VELOCITY -= 0.75
        else: 
            VELOCITY += 0.5
            self.rect.move_ip(0,VELOCITY)

        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, config.SCREEN_HEIGHT)

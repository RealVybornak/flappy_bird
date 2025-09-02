import pygame
import random

import buttons
import config

pygame.init()

pointwall = pygame.sprite.Group()
lower = pygame.sprite.Group()
upper = pygame.sprite.Group()
clouds = pygame.sprite.Group()
menu_sprites = pygame.sprite.Group()
ingame_sprites = pygame.sprite.Group()
death_sprites = pygame.sprite.Group()

def sprite_setup():
    global ADDOBSTICLE_LOWER,ADDOBSTICLE_UPPER,CLOUD,POINTWALL

    ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDOBSTICLE_UPPER, config.spawn_time)

    ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDOBSTICLE_LOWER, config.spawn_time)

    POINTWALL = pygame.USEREVENT + 3
    pygame.time.set_timer(POINTWALL, config.spawn_time)

    CLOUD = pygame.USEREVENT + 4
    pygame.time.set_timer(CLOUD, random.randint(250, 750))

    quit_button = buttons.Quit()
    menu_sprites.add(quit_button)

    start_button = buttons.Start()
    menu_sprites.add(start_button)

    menu_button = buttons.Menu()
    death_sprites.add(menu_button)

    retry_button = buttons.Retry()
    death_sprites.add(retry_button)

    game_name = buttons.Title()
    menu_sprites.add(game_name)

    dummy = buttons.Dummy_bird()
    menu_sprites.add(dummy)

sprite_setup()




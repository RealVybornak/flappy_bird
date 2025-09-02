import pygame
from pygame.locals import QUIT,K_ESCAPE,MOUSEBUTTONDOWN,KEYDOWN

import sys
sys.path.insert(1, 'C://Users//PC//OneDrive//Plocha//learning_python//flappy_bird//src//my_application//models')

import spawn_setup
import clouds_class
import pipes
import point_entity
import flappy

sys.path.insert(1, 'C://Users//PC//OneDrive//Plocha//learning_python//flappy_bird//src//my_application//models')
import sound_manager

sounds = sound_manager.Sound_manager()
sounds.load_sound("pipe_collision.mp3","assets/sounds")
sounds.load_sound("point_gain.mp3","assets/sounds")

spawn_setup.sprite_setup()

player = flappy.Player()

class Event_handler():
    def __init__(self):
        pass

    def event_handle():
        spawn_setup.sprite_setup()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit = 1
                    running = False

            elif event.type == QUIT:
                    quit = 1
                    running = False

            elif event.type == spawn_setup.ADDOBSTICLE_LOWER:
                new_lower_obsticle = pipes.Obsticles_Lower()
                spawn_setup.lower.add(new_lower_obsticle)
                spawn_setup.ingame_sprites.add(new_lower_obsticle)

            elif event.type == spawn_setup.ADDOBSTICLE_UPPER:
                new_upper_obsticle = pipes.Obsticles_Upper()
                spawn_setup.upper.add(new_upper_obsticle)
                spawn_setup.ingame_sprites.add(new_upper_obsticle)

            elif event.type == spawn_setup.POINTWALL:
                new_point = point_entity.Points()
                spawn_setup.pointwall.add(new_point)
                spawn_setup.ingame_sprites.add(new_point)

            elif event.type == spawn_setup.CLOUD:
                new_cloud = clouds_class.Clouds()
                spawn_setup.clouds.add(new_cloud)
                spawn_setup.ingame_sprites.add(new_cloud)

                if pygame.sprite.spritecollide(player, lower, upper):
                    sounds.play_sound("pipe_collision.mp3")
                    player.kill()
                    death = True
                    running = False

                if pygame.sprite.spritecollide(player, upper, lower):
                    sounds.play_sound("pipe_collision.mp3")
                    player.kill()
                    death = True
                    running = False

                if pygame.sprite.spritecollide(player, pointwall, True):
                    sounds.play_sound("point_gain.mp3")
                    score += 1
                    real_score += 1

                if pygame.sprite.groupcollide(pointwall, clouds, False, True):
                    new_cloud.kill()

"""Flappy Bird game implemented in Python using Pygame package"""

import random
import pygame
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

global y
global size_lower

score = 0

pygame.init()

screen_width = 1920
screen_height = 1080

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("flappy.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(center=(screen_width / 2, screen_height / 2))

    def movement(self, pressd_keys):
        global y
        if pressd_keys[K_SPACE]:
            y = 0
            self.rect.move_ip(0, -20)
            if pressd_keys == KEYDOWN:
                if pressd_keys == [K_ESCAPE]:
                    self.rect.move_ip(0, 20)

        else:
            try:
                if y == False:
                    y = 1
            except:
                y = 1
            y += 2
            if y < 100:
                self.rect.move_ip(0, y / 4)
            else:
                y = 100
                self.rect.move_ip(0, y / 4)

        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, screen_height)


class Obsticles_Lower(pygame.sprite.Sprite):
    def __init__(self):
        global size_lower
        super(Obsticles_Lower, self).__init__()
        size_lower = random.randint(100, 780)
        self.surf = pygame.image.load("pipe_lower.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(screen_width + 100, screen_height - size_lower / 2)
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class Obsticles_Upper(pygame.sprite.Sprite):
    def __init__(self):
        super(Obsticles_Upper, self).__init__()
        self.surf = pygame.image.load("pipe_upper.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(screen_width + 100, 0 + (screen_height - size_lower - 850) / 2)
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class Points(pygame.sprite.Sprite):
    def __init__(self):
        super(Points, self).__init__()
        self.surf = pygame.Surface((50, 1080))
        self.surf.fill((135, 206, 250))
        self.rect = self.surf.get_rect(center=(screen_width + 100, 540))

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        super(Clouds, self).__init__()
        self.surf = pygame.image.load("cloud_2.png").convert()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(screen_width + 100, random.randint(50, 1030))
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

player = Player()

pointwall = pygame.sprite.Group()
lower = pygame.sprite.Group()
upper = pygame.sprite.Group()
clouds = pygame.sprite.Group()
sprites = pygame.sprite.Group()
sprites.add(player)

running = True

ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
pygame.time.set_timer(ADDOBSTICLE_UPPER, 3500)

ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
pygame.time.set_timer(ADDOBSTICLE_LOWER, 3500)

POINTWALL = pygame.USEREVENT + 3
pygame.time.set_timer(POINTWALL, 3500)

CLOUD = pygame.USEREVENT + 4
pygame.time.set_timer(CLOUD, random.randint(750, 2000))

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADDOBSTICLE_LOWER:
            new_lower_obsticle = Obsticles_Lower()
            lower.add(new_lower_obsticle)
            sprites.add(new_lower_obsticle)

        elif event.type == ADDOBSTICLE_UPPER:
            new_upper_obsticle = Obsticles_Upper()
            upper.add(new_upper_obsticle)
            sprites.add(new_upper_obsticle)

        elif event.type == POINTWALL:
            new_point = Points()
            pointwall.add(new_point)
            sprites.add(new_point)

        elif event.type == CLOUD:
            new_cloud = Clouds()
            clouds.add(new_cloud)
            sprites.add(new_cloud)

    pressed_keys = pygame.key.get_pressed()
    player.movement(pressed_keys)

    lower.update()
    upper.update()
    pointwall.update()
    clouds.update()

    screen.fill((135, 206, 250))

    for entity in sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollide(player, lower, upper):
        player.kill()
        running = False

    if pygame.sprite.spritecollide(player, upper, lower):
        player.kill()
        running = False

    if pygame.sprite.spritecollide(player, pointwall, pointwall):
        score += 1
        print(score)
        new_point.kill()

    if pygame.sprite.groupcollide(pointwall, clouds, False, True):
        new_cloud.kill()

    pygame.display.flip()

    clock.tick(60)

try:
    if HighestScore > 99999999999:
        print("damn")
    else:
        print("=" * 50)
except:
    HighestScore = 0

if HighestScore < score:
    HighestScore = int(score)
    print("New highest score achived", HighestScore)

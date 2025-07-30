"""Flappy Bird game implemented in Python using Pygame package"""

import random
import pygame
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

global SPEED
global SPAWN_TIME

REAL_SCORE = 0
SCORE = 0
SPEED = 5
SPAWN_TIME = 3478



print("\n")
print(pygame.font.get_fonts())
print("\n")

pygame.init()
pygame.font.init()

# Score counter variables
score_font = pygame.font.SysFont('segoescript', 75, True)
black = (0,0,0)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

def draw_text(text, font, text_color, x_coords, y_coords):
    img = font.render(text, True, text_color)
    screen.blit(img, (x_coords,y_coords))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    global GRAVITY
    GRAVITY = 1
    print(GRAVITY)
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("flappy.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    

    def movement(self, pressd_keys):
        global GRAVITY
        if pressd_keys[K_SPACE]:
            GRAVITY = 0
            self.rect.move_ip(0, -20)
        else: 
            GRAVITY += 0.5
            self.rect.move_ip(0,GRAVITY)


        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, SCREEN_HEIGHT)


class Obsticles_Lower(pygame.sprite.Sprite):
    def __init__(self):
        global size
        super(Obsticles_Lower, self).__init__()
        size = random.randint(695,1365)
        self.surf = pygame.image.load("pipe_lower.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH + 100, size)
        )


    def update(self):
        self.rect.move_ip(-SPEED, 0)
        if self.rect.right < 0:
            self.kill()


class Obsticles_Upper(pygame.sprite.Sprite):
    def __init__(self):
        super(Obsticles_Upper, self).__init__()
        self.surf = pygame.image.load("pipe_upper.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH + 100, (size - 780-250))
        )

    def update(self):
        self.rect.move_ip(-SPEED, 0)
        if self.rect.right < 0:
            self.kill()


class Points(pygame.sprite.Sprite):
    def __init__(self):
        super(Points, self).__init__()
        self.surf = pygame.Surface((50, 1080))
        self.surf.fill((135, 0, 250))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH + 100, 540))

    def update(self):
        self.rect.move_ip(-SPEED, 0)
        if self.rect.right < 0:
            self.kill()


class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        super(Clouds, self).__init__()
        self.surf = pygame.image.load("cloud_2.png").convert()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH + 100, random.randint(50, 1030))
        )

    def update(self):
        self.rect.move_ip(-SPEED, 0)
        if self.rect.right < 0:
            self.kill()


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

pointwall = pygame.sprite.Group()
lower = pygame.sprite.Group()
upper = pygame.sprite.Group()
clouds = pygame.sprite.Group()
sprites = pygame.sprite.Group()
sprites.add(player)

running = True

ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
pygame.time.set_timer(ADDOBSTICLE_UPPER, SPAWN_TIME)

ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
pygame.time.set_timer(ADDOBSTICLE_LOWER, SPAWN_TIME)

POINTWALL = pygame.USEREVENT + 3
pygame.time.set_timer(POINTWALL, SPAWN_TIME)

CLOUD = pygame.USEREVENT + 4
pygame.time.set_timer(CLOUD, random.randint(250, 750))

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

    draw_text(str(REAL_SCORE), score_font, black, SCREEN_WIDTH/2, 100)

    for entity in sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollide(player, lower, upper):
        player.kill()
        running = False

    if pygame.sprite.spritecollide(player, upper, lower):
        player.kill()
        running = False

    if pygame.sprite.spritecollide(player, pointwall, True):
        SCORE += 1
        REAL_SCORE += 1
        new_point.kill()

    if pygame.sprite.groupcollide(pointwall, clouds, False, True):
        new_cloud.kill()

    if SCORE == 10:
        SPEED = 7
        SPAWN_TIME = 2513
        ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDOBSTICLE_UPPER, SPAWN_TIME)

        ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
        pygame.time.set_timer(ADDOBSTICLE_LOWER, SPAWN_TIME)

        POINTWALL = pygame.USEREVENT + 3
        pygame.time.set_timer(POINTWALL, SPAWN_TIME)
        SCORE += 1
    if SCORE == 25:
        SPEED = 9
        SPAWN_TIME = 1977
        ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDOBSTICLE_UPPER, SPAWN_TIME)

        ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
        pygame.time.set_timer(ADDOBSTICLE_LOWER, SPAWN_TIME)

        POINTWALL = pygame.USEREVENT + 3
        pygame.time.set_timer(POINTWALL, SPAWN_TIME)
        SCORE += 1
    if SCORE == 50:
        SPEED = 13
        SPAWN_TIME = 1400
        ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDOBSTICLE_UPPER, SPAWN_TIME)

        ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
        pygame.time.set_timer(ADDOBSTICLE_LOWER, SPAWN_TIME)

        POINTWALL = pygame.USEREVENT + 3
        pygame.time.set_timer(POINTWALL, SPAWN_TIME)
        SCORE += 1
    if SCORE == 100:
        SPEED = 50
        SPAWN_TIME = 400
        ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDOBSTICLE_UPPER, SPAWN_TIME)

        ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
        pygame.time.set_timer(ADDOBSTICLE_LOWER, SPAWN_TIME)

        POINTWALL = pygame.USEREVENT + 3
        pygame.time.set_timer(POINTWALL, SPAWN_TIME)
        SCORE += 1
    pygame.display.flip()

    clock.tick(60)

#try:
#    if HighestScore > 99999999999:
#        print("damn")
#    else:
#        print("=" * 50)
#except:
#    HighestScore = 0
#
#if HighestScore < score:
#    HighestScore = int(score)
#    print("New highest score achived", HighestScore)
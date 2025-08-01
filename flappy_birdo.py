"""Flappy Bird game implemented in Python using Pygame package"""
import random
import pygame
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)

global SPEED
global SPAWN_TIME

# Variables
REAL_SCORE = 0
SCORE = 0
SPEED = 5
SPAWN_TIME = 2000

pygame.init()
pygame.font.init()

# Score counter variables
score_font = pygame.font.SysFont('segoescript', 75, True)
black = (0,0,0)

# Size of the window
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


# Function for text to apear on screen
def draw_text(text, font, text_color, x_coords, y_coords):
    img = font.render(text, True, text_color)
    screen.blit(img, (x_coords,y_coords))

# Used for tick speed
clock = pygame.time.Clock()

# Classes
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
        self.surf = pygame.Surface((50, SCREEN_HEIGHT))
        self.surf.fill((135, 0, 250))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH + 100, SCREEN_HEIGHT/2))

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
            
class Start(pygame.sprite.Sprite):
    def __init__(self):
        super(Start, self).__init__()
        self.surf = pygame.image.load("start_button.png").convert()
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(1320, 750)
        )

class Quit(pygame.sprite.Sprite):
    def __init__(self):
        super(Quit, self).__init__()
        self.surf = pygame.image.load("quit_button.png").convert()
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(600, 750)
        )

class Title(pygame.sprite.Sprite):
    def __init__(self):
        super(Title, self).__init__()
        self.surf = pygame.image.load("Title_name.png").convert()
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(960,300)
        )

class Dummy_bird(pygame.sprite.Sprite):
    def __init__(self):
        super(Dummy_bird, self).__init__()
        self.surf = pygame.image.load("dummy_flappy.png").convert()
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(960,500)
        )
    

# Window set up
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Creating a player 
player = Player()

# Groups
pointwall = pygame.sprite.Group()
lower = pygame.sprite.Group()
upper = pygame.sprite.Group()
clouds = pygame.sprite.Group()
menu_sprites = pygame.sprite.Group()
ingame_sprites = pygame.sprite.Group()
ingame_sprites.add(player)

# Set up for Main game loop and Menu game loop
running = True
menu = True

# Spawning each sprite for class
ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
pygame.time.set_timer(ADDOBSTICLE_UPPER, SPAWN_TIME)

ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
pygame.time.set_timer(ADDOBSTICLE_LOWER, SPAWN_TIME)

POINTWALL = pygame.USEREVENT + 3
pygame.time.set_timer(POINTWALL, SPAWN_TIME)

CLOUD = pygame.USEREVENT + 4
pygame.time.set_timer(CLOUD, random.randint(250, 750))

quit_button = Quit()
menu_sprites.add(quit_button)

start_button = Start()
menu_sprites.add(start_button)

game_name = Title()
menu_sprites.add(game_name)

dummy = Dummy_bird()
menu_sprites.add(dummy)

# Menu loop
while menu:
    screen.fill((135, 206, 250))
    for menu_enitity in  menu_sprites:
        screen.blit(menu_enitity.surf, menu_enitity.rect)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                menu = False

        elif event.type == QUIT:
            running = False
            menu = False

        elif event.type == MOUSEBUTTONDOWN:
            cursor_position = pygame.mouse.get_pos()

            if 1019 < cursor_position[0] < 1619:
                if 600 < cursor_position[1] < 898:
                    menu = False

            if 300 < cursor_position[0] < 889:
                if 600 < cursor_position[1] < 897:
                    menu = False
                    running = False

    pygame.display.flip()

# Main game loop
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
            ingame_sprites.add(new_lower_obsticle)

        elif event.type == ADDOBSTICLE_UPPER:
            new_upper_obsticle = Obsticles_Upper()
            upper.add(new_upper_obsticle)
            ingame_sprites.add(new_upper_obsticle)

        elif event.type == POINTWALL:
            new_point = Points()
            pointwall.add(new_point)
            ingame_sprites.add(new_point)

        elif event.type == CLOUD:
            new_cloud = Clouds()
            clouds.add(new_cloud)
            ingame_sprites.add(new_cloud)


    # Movement for player
    pressed_keys = pygame.key.get_pressed()
    player.movement(pressed_keys)

    # Movement for other sprites
    lower.update()
    upper.update()
    pointwall.update()
    clouds.update()

    # Background
    screen.fill((135, 206, 250))

    # Score counter
    draw_text(str(REAL_SCORE), score_font, black, SCREEN_WIDTH/2, 100)

    # Drawing every sprite
    for entity in ingame_sprites:
        screen.blit(entity.surf, entity.rect)

    # Collisions between sprites
    if pygame.sprite.spritecollide(player, lower, upper):
        player.kill()
        running = False

    if pygame.sprite.spritecollide(player, upper, lower):
        player.kill()
        running = False

    if pygame.sprite.spritecollide(player, pointwall, True):
        SCORE += 1
        REAL_SCORE += 1


    if pygame.sprite.groupcollide(pointwall, clouds, False, True):
        new_cloud.kill()

    # Difficulty increase (speed and spawn time is changed)
    if SCORE == 10:
        SPEED = 7
        SPAWN_TIME = 1400
        ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDOBSTICLE_UPPER, SPAWN_TIME)

        ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
        pygame.time.set_timer(ADDOBSTICLE_LOWER, SPAWN_TIME)

        POINTWALL = pygame.USEREVENT + 3
        pygame.time.set_timer(POINTWALL, SPAWN_TIME)
        SCORE += 1
    if SCORE == 25:
        SPEED = 9
        SPAWN_TIME = 1200
        ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDOBSTICLE_UPPER, SPAWN_TIME)

        ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
        pygame.time.set_timer(ADDOBSTICLE_LOWER, SPAWN_TIME)

        POINTWALL = pygame.USEREVENT + 3
        pygame.time.set_timer(POINTWALL, SPAWN_TIME)
        SCORE += 1
    if SCORE == 50:
        SPEED = 13
        SPAWN_TIME = 900
        ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDOBSTICLE_UPPER, SPAWN_TIME)

        ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
        pygame.time.set_timer(ADDOBSTICLE_LOWER, SPAWN_TIME)

        POINTWALL = pygame.USEREVENT + 3
        pygame.time.set_timer(POINTWALL, SPAWN_TIME)
        SCORE += 1
    if SCORE == 100:
        SPEED = 25
        SPAWN_TIME = 800
        ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDOBSTICLE_UPPER, SPAWN_TIME)

        ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
        pygame.time.set_timer(ADDOBSTICLE_LOWER, SPAWN_TIME)

        POINTWALL = pygame.USEREVENT + 3
        pygame.time.set_timer(POINTWALL, SPAWN_TIME)
        SCORE += 1
    
    # Making everting work
    pygame.display.flip()

    # Setting tickspeed
    clock.tick(60)
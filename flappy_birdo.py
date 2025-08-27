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

# Preperations for saving and loading the highest score
try:
    fc = open('Highest_score.txt','x')
except:
    print("\n")
else:
    with open('Highest_score.txt','w') as f:
        f.write("0")

FILE = open('Highest_score.txt')
INFILE_SCORE = FILE.read()
highest_score = int(INFILE_SCORE)

# Variables
real_score = 0
score = 0
speed = 5                           
spawn_time = 2000

pygame.mixer.init()
pygame.init()
pygame.font.init()

# Score counter variables
score_font = pygame.font.SysFont('segoescript', 75, True)
black = (0,0,0)

# Setting up images for classes
PLAYER_IMG = pygame.image.load("assets/textures/flappy.png")
LOWER_PIPE_IMG = pygame.image.load("assets/textures/pipe_lower.png")
UPPER_PIPE_IMG = pygame.image.load("assets/textures/pipe_upper.png")
CLOUD_IMG = pygame.image.load("assets/textures/cloud_2.png")

START_IMG = pygame.image.load("assets/textures/start_button.png")
QUIT_IMG = pygame.image.load("assets/textures/quit_button.png")
MENU_IMG = pygame.image.load("assets/textures/menu_button.png")
RETRY_IMG = pygame.image.load("assets/textures/retry_button.png")

TITLE_IMG = pygame.image.load("assets/textures/title_name.png")
DUMMY_IMG = pygame.image.load("assets/textures/dummy_flappy.png")

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
    global VELOCITY
    VELOCITY = 1
    def __init__(self):
        super().__init__()
        self.surf = PLAYER_IMG
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    def movement(self, pressd_keys):
        global VELOCITY
        if pressd_keys[K_SPACE]:
            wing_flap.play()
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
        self.rect.bottom = min(self.rect.bottom, SCREEN_HEIGHT)


class Obsticles_Lower(pygame.sprite.Sprite):
    def __init__(self):
        global size
        super().__init__()
        size = random.randint(695,1365)
        self.surf = LOWER_PIPE_IMG
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH + 100, size)
        )


    def update(self):
        self.rect.move_ip(-speed, 0)
        if self.rect.right < 0:
            self.kill()


class Obsticles_Upper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = UPPER_PIPE_IMG
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH + 100, (size - 780-250))
        )

    def update(self):
        self.rect.move_ip(-speed, 0)
        if self.rect.right < 0:
            self.kill()


class Points(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, SCREEN_HEIGHT))
        self.surf.fill((135, 0, 250))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH + 100, SCREEN_HEIGHT/2))

    def update(self):
        self.rect.move_ip(-speed, 0)
        if self.rect.right < 0:
            self.kill()


class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = CLOUD_IMG
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH + 100, random.randint(50, 1030))
        )

    def update(self):
        self.rect.move_ip(-speed, 0)
        if self.rect.right < 0:
            self.kill()
            
class Start(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = START_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(1320, 750)
        )

class Quit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = QUIT_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(600, 750)
        )

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = MENU_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(1320, 750)
        )

class Retry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = RETRY_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(600, 750)
        )


class Title(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = TITLE_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(990,300)
        )

class Dummy_bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = DUMMY_IMG
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(
            center=(960,435)
        )

#class Score_manager():
#    def __init__(self):
            
    

# Window set up
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Creating a player 
player = Player()

# Creating groups
pointwall = pygame.sprite.Group()
lower = pygame.sprite.Group()
upper = pygame.sprite.Group()
clouds = pygame.sprite.Group()
menu_sprites = pygame.sprite.Group()
ingame_sprites = pygame.sprite.Group()
ingame_sprites.add(player)
death_sprites = pygame.sprite.Group()

# Set up for Game loop
main_loop = True
running = False
menu = True
death = False
quit = 0

# Setting up each sprite for class and their timers
ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
pygame.time.set_timer(ADDOBSTICLE_UPPER, spawn_time)

ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
pygame.time.set_timer(ADDOBSTICLE_LOWER, spawn_time)

POINTWALL = pygame.USEREVENT + 3
pygame.time.set_timer(POINTWALL, spawn_time)

CLOUD = pygame.USEREVENT + 4
pygame.time.set_timer(CLOUD, random.randint(250, 750))

quit_button = Quit()
menu_sprites.add(quit_button)

start_button = Start()
menu_sprites.add(start_button)

menu_button = Menu()
death_sprites.add(menu_button)

retry_button = Retry()
death_sprites.add(retry_button)

game_name = Title()
menu_sprites.add(game_name)

dummy = Dummy_bird()
menu_sprites.add(dummy)

# Setting up sounds effects and background music
pygame.mixer.music.load("assets/sounds/background.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)

collision_sound = pygame.mixer.Sound("assets/sounds/pipe_collision.mp3")
point_gained = pygame.mixer.Sound("assets/sounds/point_gain.mp3")
point_gained.set_volume(0.75)
wing_flap = pygame.mixer.Sound("assets/sounds/wing_flap.mp3")
wing_flap.set_volume(0.2)
mouse_click = pygame.mixer.Sound("assets/sounds/mouse_click.mp3")

while main_loop:
    # Menu loop
    while menu:
        screen.fill((135, 206, 250))
        for menu_enitity in  menu_sprites:
            screen.blit(menu_enitity.surf, menu_enitity.rect)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit = 1
                    menu = False


            elif event.type == QUIT:
                quit = 1
                menu = False

            elif event.type == MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()

                if 1019 < cursor_position[0] < 1619:
                    if 600 < cursor_position[1] < 898:
                        mouse_click.play()
                        running = True
                        menu = False   

                if 300 < cursor_position[0] < 889:
                    if 600 < cursor_position[1] < 897:
                        mouse_click.play()
                        quit = 1
                        menu = False


        pygame.display.flip()

    # Mechanism for turning of the game
    if quit == 1:
        break

    # Main game loop
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit = 1
                    running = False

            elif event.type == QUIT:
                    quit = 1
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
        draw_text(str(real_score), score_font, black, SCREEN_WIDTH/2, 100)

        # Drawing every sprite
        for entity in ingame_sprites:
            screen.blit(entity.surf, entity.rect)

        # Collisions between sprites
        if pygame.sprite.spritecollide(player, lower, upper):
            collision_sound.play()
            player.kill()
            death = True
            running = False

        if pygame.sprite.spritecollide(player, upper, lower):
            collision_sound.play()
            player.kill()
            death = True
            running = False

        if pygame.sprite.spritecollide(player, pointwall, True):
            point_gained.stop()
            point_gained.play()
            score += 1
            real_score += 1

        if pygame.sprite.groupcollide(pointwall, clouds, False, True):
            new_cloud.kill()

        # Difficulty increase (speed and spawn time is changed)
        if score == 10:
            speed = 7
            spawn_time = 1400
            ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
            pygame.time.set_timer(ADDOBSTICLE_UPPER, spawn_time)

            ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
            pygame.time.set_timer(ADDOBSTICLE_LOWER, spawn_time)

            POINTWALL = pygame.USEREVENT + 3
            pygame.time.set_timer(POINTWALL, spawn_time)
            score += 1
        if score == 26:
            speed = 9
            spawn_time = 1200
            ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
            pygame.time.set_timer(ADDOBSTICLE_UPPER, spawn_time)

            ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
            pygame.time.set_timer(ADDOBSTICLE_LOWER, spawn_time)

            POINTWALL = pygame.USEREVENT + 3
            pygame.time.set_timer(POINTWALL, spawn_time)
            score += 1
        if score == 52:
            speed = 13
            spawn_time = 900
            ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
            pygame.time.set_timer(ADDOBSTICLE_UPPER, spawn_time)

            ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
            pygame.time.set_timer(ADDOBSTICLE_LOWER, spawn_time)

            POINTWALL = pygame.USEREVENT + 3
            pygame.time.set_timer(POINTWALL, spawn_time)
            score += 1
        if score == 103:
            speed = 25
            spawn_time = 800
            ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
            pygame.time.set_timer(ADDOBSTICLE_UPPER, spawn_time)

            ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
            pygame.time.set_timer(ADDOBSTICLE_LOWER, spawn_time)

            POINTWALL = pygame.USEREVENT + 3
            pygame.time.set_timer(POINTWALL, spawn_time)
            score += 1
        
        # Making everting work
        pygame.display.flip()

        # Setting tickspeed
        clock.tick(60)

    # Mechanism for turning of the game
    if quit == 1:
        break

    while death:
        screen.fill((135, 206, 250))
        for death_enitity in death_sprites:
            screen.blit(death_enitity.surf, death_enitity.rect)

        try:          
            if highest_score < real_score:
                decoy_highest_score = real_score
                new_score = str(real_score)
                with open('Highest_score.txt','w') as f:
                    f.write(new_score)
                    print("new score")
            else: 
                decoy_highest_score = highest_score
        except:
            print("u are cooked")
        

        draw_text(f"Highest achived score: {str(decoy_highest_score)}", score_font, black, SCREEN_WIDTH/2-480, 200)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit = 1
                    death = False


            elif event.type == QUIT:
                quit = 1
                death = False

            elif event.type == MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()

                if 1019 < cursor_position[0] < 1619:
                    if 600 < cursor_position[1] < 898:
                        mouse_click.play()
                        menu = True
                        death = False 

                if 300 < cursor_position[0] < 889:
                    if 600 < cursor_position[1] < 897:
                        mouse_click.play()
                        running = True
                        death = False


        pygame.display.flip()

    # Respawning player 
    player = Player()

    # Reseting variables
    real_score = 0
    score = 0
    speed = 5
    spawn_time = 2000

    # Restarting groups
    pointwall = pygame.sprite.Group()
    lower = pygame.sprite.Group()
    upper = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    menu_sprites = pygame.sprite.Group()
    ingame_sprites = pygame.sprite.Group()
    ingame_sprites.add(player)

    # Restarting timers and each sprite in a class
    ADDOBSTICLE_UPPER = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDOBSTICLE_UPPER, spawn_time)

    ADDOBSTICLE_LOWER = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDOBSTICLE_LOWER, spawn_time)

    POINTWALL = pygame.USEREVENT + 3
    pygame.time.set_timer(POINTWALL, spawn_time)

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
    
    # Mechanism for turning of the game
    if quit == 1:
        break



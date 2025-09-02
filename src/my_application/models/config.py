import pygame
pygame.font.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

SCORE_FONT = pygame.font.SysFont('segoescript', 75, True)
BLACK = (0,0,0)

BUTTON_Y = (600,900)
RIGHT_BUTTON_X = (1020,1620)
LEFT_BUTTON_X = (300,890)

real_score = 0
score = 0
speed = 5                           
spawn_time = 2000
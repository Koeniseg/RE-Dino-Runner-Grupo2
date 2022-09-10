import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FRONT_STYLE = 'freesansbold.ttf'
menu_color = (0, 128, 128)

def get_score_element(points):
    font = pygame.font.Font(FRONT_STYLE, 25)
    text = font.render('Points: ' + str(points), True, menu_color)
    text_rect = text.get_rect()
    text_rect.center = (975, 40)
    return text, text_rect

def get_menu_data(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FRONT_STYLE, 30)
    text = font.render(message, True, menu_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect

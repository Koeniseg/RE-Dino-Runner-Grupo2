import pygame

FRONT_STYLE = 'freesansbold.ttf'
menu_color = (128, 0, 0)

def get_score_element(points):
    font = pygame.font.Font(FRONT_STYLE, 25)
    text = font.render('Points: ' + str(points), True, menu_color)
    text_rect = text.get_rect()
    text_rect.center = (975, 40)
    return text, text_rect

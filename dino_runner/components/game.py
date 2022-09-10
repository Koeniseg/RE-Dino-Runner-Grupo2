import pygame


from dino_runner.components.Lifes.lifes_manager import LivesManager
from dino_runner.components.Power_up.power_up_manager import PowerUpManager
from dino_runner.components.cloud import Cloud
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.Obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.text_utiles import get_score_element, get_menu_data
from dino_runner.utils.constants import BG, CLOUD, FINAL_IMAGE, GAME_OVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.lifes_manager = LivesManager()
        self.power_up_manager = PowerUpManager()
        self.cloud = Cloud()
        self.points = 0
        self.running = True
        self.death_count = 0

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_all()
        self.lifes_manager.reset_hearts()
        self.points = 0
        self.game_speed = 20
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.cloud.update(self.game_speed)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        dg_color = (255, 255, 255) if self.points // 750 != 1 else (0, 0, 0)
        self.clock.tick(FPS)
        self.screen.fill(dg_color)
        # self.draw(self.screen, self.points)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        self.lifes_manager.draw(self.screen)
        self.score()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)
        self.player.check_invincibility(self.screen)
        self.player.check_hammer(self.screen)

    def show_menu(self):
        # self.running = True
        white_color = (205, 205, 205)
        self.screen.fill(white_color)

        self.print_menu_elements(self.death_count)
        pygame.display.update()

        self.handle_key_events_on_menu()

    def print_menu_elements(self, death_count = 0):
        if death_count == 0:
            self.screen.blit(ICON, (500, 150))
            self.screen.blit(CLOUD, (450, 160))
            self.screen.blit(CLOUD, (560, 195))
            text, text_rect = get_menu_data('Press any key to start the game')
            self.screen.blit(text, text_rect)
        elif death_count > 0:
            self.screen.blit(GAME_OVER, (370, 240))
            self.screen.blit(FINAL_IMAGE, (450, 110))
            text, text_rect = get_menu_data('Press any key to restart game')
            self.screen.blit(text, text_rect)
            text_death, text_death_rect = get_menu_data('Deaths: {}'.format(death_count), 550, 350)
            self.screen.blit(text_death, text_death_rect)
            text_point, text_point_rect = get_menu_data('Points: {}'.format(self.points), 550, 400)
            self.screen.blit(text_point, text_point_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


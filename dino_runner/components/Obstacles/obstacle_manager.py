import pygame
import random

from dino_runner.components.Obstacles.obstacles import SmallCactus, LargeCactus, Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        self.tries = 5

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                else:
                    self.tries -= 1
                    game.lifes_manager.reduce_heart()
                    if self.tries != 0:
                        self.obstacles.pop()
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break

    def reset_all(self):
        self.obstacles = []
        self.tries = 5

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
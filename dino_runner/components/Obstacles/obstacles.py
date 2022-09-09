import random
import pygame

from dino_runner.components.Obstacles.obstacle import Obstacle


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 330


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 305


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(250, 325)
        self.index = 0

    def draw(self, screen):
        if self.index >= 10:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1
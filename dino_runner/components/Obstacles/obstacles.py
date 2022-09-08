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


# class Bird(Obstacle):
#     def __init__(self, image):
#         super().__init__(image, self.type)
import pygame

from game_object import game_obj
from pygame import Rect


class game_obstacle(game_obj):
    def __init__(self, rect: Rect, draw_layer: int):
        super().__init__(rect, draw_layer)
        self.solid = True
        self.color = (0, 0, 255)
        self.type = "wall"


class SmallWall(game_obstacle):
    def __init__(self, pos: tuple, draw_layer=1):
        rect = pygame.Rect(pos, (50, 50))
        super().__init__(rect, draw_layer)

    def update(self):
        pass

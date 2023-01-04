from pygame import Rect
import math

class game_obj(object):
    def __init__(self, pos: list, rect: Rect, draw_layer):
        self.pos = pos
        self.rect = rect
        self.draw_layer = draw_layer
        self.solid = False

class game_obj_move(game_obj):
    def __init__(self, pos: list, rect: Rect, draw_layer, dir: int):
        super().__init__(pos, rect, draw_layer)
        self.dir = dir
        self.solid = True

    def move(self, angle, speed):
        step = [(math.sin(angle)) * speed, (math.cos(angle)) * speed]
        #todo Check if next position is feasable. If so, go there. If not: speed = 0
        self.pos[0] += step[0]
        self.pos[1] += step[1]
        self.rect.move_ip(step[0], step[1])


class game_obstacle(game_obj):
    def __init__(self, pos: list, rect: Rect, draw_layer):
        super().__init__(pos, rect, draw_layer)
        self.solid = True

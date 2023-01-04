from pygame import Rect
import math

class game_obj(object):
    def __init__(self, pos: list, rect: Rect, draw_layer):
        self.pos = pos
        self.rect = rect
        self.draw_layer = draw_layer
        self.solid = False
        self.type = ""

class game_obj_move(game_obj):
    def __init__(self, pos: list, rect: Rect, draw_layer, dir: int):
        super().__init__(pos, rect, draw_layer)
        self.dir = dir
        self.solid = True
        self.collision_list = []

    def move(self, angle, speed):
        angle = math.radians(angle)
        step = [(math.sin(angle)) * speed, (math.cos(angle)) * speed]
        if not self.collision_list:
        #todo Check if next position is feasable. If so, go there. If not: speed = 0
            self.pos[0] += step[0]
            self.pos[1] += step[1]
            self.rect.move_ip(step[0], step[1])

    def add_collision(self, units):
        self.collision_list = units

    def remove_collision(self):
        self.collision_list = []

from pygame import Rect
import math
from calc import *


class game_obj(object):
    def __init__(self, rect: Rect, draw_layer): #rect and pos?
        self.rect = rect
        self.draw_layer = draw_layer
        self.solid = False
        self.type = ""

class game_obj_move(game_obj):
    def __init__(self, rect: Rect, draw_layer, dir: int):
        super().__init__(rect, draw_layer)
        self.dir = dir
        self.solid = True
        self.collision_list = []

    def move(self, angle, speed):
        may_move = True
        angle = math.radians(angle)
        step = [(math.sin(angle)) * speed, (math.cos(angle)) * speed]
        if self.collision_list:
            nextpos = [ self.rect.centerx + step[0], self.rect.centery + step[1]]
            for col in self.collision_list:
                cur_dist = calculate_distance_rect(col, self)
                new_dist = calculate_distance(col.rect.center, nextpos)
                if new_dist < cur_dist:
                    may_move = False

        if may_move:
            self.rect.move_ip(step[0], step[1])

    def add_collision(self, unit):
        self.collision_list.append(unit)

    def remove_collision(self):
        self.collision_list = []

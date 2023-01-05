import json
from enum import Enum
import time

from game_object import game_obj_move
import math

class Unit(game_obj_move):
    def __init__(self, rect, draw_layer, dir):
        super().__init__(rect, draw_layer, dir)
        self.angle = 90
        self.eye_sight = []
        self.hearing = []
        self.max_speed = 6 #todo magic value
        self.can_throw = False
        self.can_throw_timer = int(time.time())
        self.type = "unit"
        self.color = (255, 0, 0)

    def move(self, speed: float, angle: int):
        """moves object."""
        if abs(speed) > self.max_speed:
            speed = self.max_speed
        if speed < 0:
            speed = 0
        if angle != self.angle:
            if angle -3 < self.angle < angle +3:
                #todo with 3 degrees at 60 fps, we have 2 seconds for a full round. write this
                pass

        super().move(angle, speed)

    def change_angle(self, angle: int):
        pass

    def update(self):
        self.can_throw = self.can_throw_snowball()
        pass

    def can_throw_snowball(self):
        if not self.can_throw:
            time_now = int(time.time())
            if time_now - self.can_throw_timer > 2:  #todo every 2 seconds, magic value
                self.can_throw_timer = time_now
                return True
            return False
        else:
            return True

    def update_eye_sight(self, seen_units):
        self.eye_sight = seen_units

    def unit_update(self):
        data = {'position': self.pos,
                'angle': self.angle,
                'eye_sight': self.eye_sight,
                'can_throw': self.can_throw}
        print(json.dumps(data))

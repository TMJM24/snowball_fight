import json
from enum import Enum
import time

from game_object import game_obj_move
import math

class Unit(game_obj_move):
    def __init__(self, pos, rect, draw_layer, dir):
        super().__init__(pos, rect, draw_layer, dir)
        self.eye_sight = []
        self.hearing = []
        self.max_speed = 6 #todo magic value
        self.can_throw = False
        self.can_throw_timer = int(time.time())

    def move(self, speed: float, angle: int):
        """moves object."""
        if abs(speed) > self.max_speed:
            speed = self.max_speed #todo and with negative's?
        super().move(angle, speed)

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
                'eye_sight': self.eye_sight,
                'can_throw': self.can_throw}
        print(json.dumps(data))

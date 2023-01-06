import json
import time
from pygame import Rect
from game_object import game_obj_move
import math

class Unit(game_obj_move):
    def __init__(self, pos, angle, draw_layer=1):
        rect = Rect(pos, (50, 50))
        super().__init__(rect, draw_layer, angle)
        self.speed = 0
        self.eye_sight = []
        self.hearing = []
        self.max_speed = 6 #todo magic value
        self.can_throw = False
        self.can_throw_timer = int(time.time())
        self.type = "unit"
        self.color = (255, 0, 0)

    def move(self, speed: float, angle: int):
        """moves object."""
        if speed > self.max_speed:
            speed = self.max_speed
        if speed < -3:                      #todo magic value
            speed = -3
        self.speed = speed
        if angle > 3:
            angle = 3
        elif angle < -3:
            angle = -3
        self.angle += angle
        if self.angle >= 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360
        super().move(self.angle, self.speed)

    def update(self):
        self.can_throw = self.can_throw_snowball()
        pass

    def can_throw_snowball(self) ->bool:
        if not self.can_throw:
            time_now = int(time.time())
            if time_now - self.can_throw_timer > 2:  #todo every 2 seconds, magic value
                self.can_throw_timer = time_now
                return True
            return False
        else:
            return True

    def update_eye_sight(self, seen_units: list):
        self.eye_sight = seen_units

    def unit_update(self):
        data = {'position': self.pos,
                'angle': self.angle,
                'eye_sight': self.eye_sight,
                'can_throw': self.can_throw}
        print(json.dumps(data))

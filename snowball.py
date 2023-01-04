from game_object import game_obj_move
from pygame import Rect

class snowball(game_obj_move):
    def __init__(self, pos: list, rect: Rect, draw_layer, dir: int):
        super().__init__(pos, rect, draw_layer, dir)
        self.eye_sight = []
        self.hearing = []

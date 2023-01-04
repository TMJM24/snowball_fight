import pygame
from sightHandler import SightHandler
from collisionHandler import CollisionHandler
class GameHandler(object):
    def __init__(self):
        self.game_objects = []
        self.sight_handler = SightHandler()
        self.collision_handler = CollisionHandler()
        pass

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def remove_game_objects(self, game_object):
        pass

    def update(self, surface):
        self.sight_handler.update_eyesight(self.game_objects, surface)
        self.collision_handler.calculate_collisions(self.game_objects)

    def draw_game_objects(self, surface):
        for unit in self.game_objects:
            unit.update()
            pygame.draw.rect(surface, unit.color, unit.rect)
            if unit.type == "unit":
                pygame.draw.circle(surface, unit.color, unit.rect.center, 200, width=1)

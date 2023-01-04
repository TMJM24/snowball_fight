import pygame

class GameHandler(object):
    def __init__(self):
        self.game_objects = []
        pass

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def remove_game_objects(self, game_object):
        pass

    def draw_game_objects(self, surface):
        for unit in self.game_objects:
            unit.update()
            pygame.draw.rect(surface, (40, 0, 0, ), unit.rect)

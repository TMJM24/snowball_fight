import pygame
import math
from gamehandler import GameHandler
from sight_handler import SightHandler
from unit import Unit
from obstacles import SmallWall

from player import Player

pygame.init()
screen = pygame.display.set_mode([1920, 1080])
clock = pygame.time.Clock()

# Run until the user asks to quit
game_handler = GameHandler()
sight_handler = SightHandler()


#player_1 = Player("johan")
game_handler.add_game_object(Unit([100, 100], pygame.Rect((100, 100), (40, 40)), 1, 100))
game_handler.add_game_object(Unit([400, 150], pygame.Rect((400, 150), (40, 40)), 1, 100))
game_handler.add_game_object(SmallWall((500, 500)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #player_1.update()
    game_handler.game_objects[0].move(3, 90) #todo this is a place holder so that I can test
    game_handler.game_objects[0].unit_update()
    # Fill the background with white
    screen.fill((255, 255, 255))
    sight_handler.update_eyesight(game_handler.game_objects)
    game_handler.draw_game_objects(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

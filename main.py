import pygame
import math
from gamehandler import GameHandler
from unit import Unit
from obstacles import SmallWall

from player import Player

pygame.init()
screen = pygame.display.set_mode([1920, 1080])
clock = pygame.time.Clock()

# Run until the user asks to quit
game_handler = GameHandler()


#player_1 = Player("johan")
game_handler.add_game_object(Unit(pygame.Rect((100, 100), (40, 40)), 1, 100))
game_handler.add_game_object(Unit(pygame.Rect((400, 200), (40, 40)), 1, 100))
game_handler.add_game_object(SmallWall((800, 100)))
game_handler.add_game_object(SmallWall((400, 200)))
#game_handler.game_objects[1].angle = 270

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    #player_1.update()
    game_handler.game_objects[0].move(3, 90) #todo this is a place holder so that I can test
    game_handler.update(screen)
    #game_handler.game_objects[0].unit_update() #todo turned off, this is json output
    game_handler.draw_game_objects(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

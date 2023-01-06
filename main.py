import pygame
from manualPlayer import ManualPlayer
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
game_handler.add_game_object(Unit((680, 100), 0))
game_handler.add_game_object(ManualPlayer((700, 700), 90))

game_handler.add_game_object(SmallWall((800, 100)))
game_handler.add_game_object(SmallWall((600, 200)))
game_handler.add_game_object(SmallWall((800, 150)))
game_handler.add_game_object(SmallWall((800, 200)))

pygame.event.set_blocked(None) #block all events
pygame.event.set_allowed(pygame.QUIT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    game_handler.update(screen)
    #game_handler.game_objects[0].unit_update() #todo turned off, this is json output example
    game_handler.draw_game_objects(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

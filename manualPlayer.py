import pygame
from unit import Unit


class ManualPlayer(Unit):
    def __init__(self, pos: tuple, angle: int):
        super().__init__(pos, angle)

    def move_player(self):
        """This is a listner to the keyboard, so that you can run an instance yourself. """
        speed = 0
        angle = 0
        command = pygame.key.get_pressed()
        if command[pygame.K_UP]:
            speed = 5
        elif command[pygame.K_DOWN]:
            speed = -2
        if command[pygame.K_LEFT]:
            angle = 2
        elif command[pygame.K_RIGHT]:
            angle = - 2

        self.move(speed, angle)

    def update(self):
        self.move_player()
        super().update()

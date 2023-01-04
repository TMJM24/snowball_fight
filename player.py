import os
from enum import Enum, auto
import posix
import errno


class Player(object):
    def __init__(self, player_name):
        self.state = player_states.CONNECTING
        self.player_name = player_name
        input_name = f"command_interface_{player_name}"
        try:
            os.mkfifo(input_name)
        except FileExistsError:
            pass
        self.input = open(input_name)
        #self.input.write("a start")

    def get_update(self):
        pass

    def update(self):
        if self.state == player_states.CONNECTING:
            input = self.input.read()
            if len(input):
                if input == "hello world\n":
                    print("success! with connection")
                    self.state = player_states.WAITING
        elif self.state == player_states.WAITING:
            pass                        #todo



class player_states(Enum):
    CONNECTING = auto()
    WAITING = auto()
    PLAYING = auto()
    END_GAME = auto()


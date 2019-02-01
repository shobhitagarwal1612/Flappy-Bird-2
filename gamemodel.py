import weakref

from pyglet.event import EventDispatcher

import levels
from layers.bird import Bird
from status import status

__all__ = ['GameModel']


#
# Model (of the MVC pattern)
#

class GameModel(EventDispatcher):

    def __init__(self):
        super(GameModel, self).__init__()

        self.bird = None
        self.pipes = {}

        self.init()

        status.reset()

        status.level = levels.levels[0]

    def set_controller(self, ctrl):
        self.ctrl = weakref.ref(ctrl)

    def flap_wings(self):
        self.bird.flap_flap()

    def start(self):
        self.set_next_level()

    def set_next_level(self):
        self.ctrl().resume_controller()

        if status.level_idx is None:
            status.level_idx = 0
        else:
            status.level_idx += 1

        l = levels.levels[status.level_idx]

        self.init()
        status.level = l()

        self.get_random_pipe()

        self.dispatch_event("on_new_level")

    def move_pipes(self):
        pass

    def init(self):
        self.bird = Bird()
        self.bird.set_initial_speed()

    def get_random_pipe(self):
        pass


GameModel.register_event_type('on_new_level')
GameModel.register_event_type('on_game_over')
GameModel.register_event_type('on_flap_wings')

from cocos.layer import Layer
from pyglet.window import key

from status import status

__all__ = ['GameCtrl']


#
# Controller ( MVC )
#

class GameCtrl(Layer):
    is_event_handler = True  #: enable pyglet's events

    def __init__(self, model):
        super(GameCtrl, self).__init__()

        self.used_key = False
        self.paused = True

        self.model = model
        self.elapsed = 0

    def on_key_press(self, k, m):
        if self.paused:
            return False

        if self.used_key:
            return False

        if k in (key.ENTER, key.SPACE, key.UP):
            self.model.flap_wings()
            self.used_key = True
            return True
        return False

    def pause_controller(self):
        """removes the schedule timer and doesn't handler the keys"""

        print('paused')
        self.paused = True
        self.unschedule(self.step)

    def resume_controller(self):
        """schedules  the timer and handles the keys"""

        print('resumed')
        self.paused = False
        self.schedule(self.step)

    def step(self, dt):
        """updates the engine"""

        print('step ticker')
        self.elapsed += dt
        if self.elapsed > status.level.speed:
            self.elapsed = 0
            self.model.move_pipes()

    def draw(self):
        """draw the map and the block"""

        self.used_key = False

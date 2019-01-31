from pyglet.event import EventDispatcher

__all__ = ['GameModel']


#
# Model (of the MVC pattern)
#

class GameModel(EventDispatcher):

    def __init__(self):
        super(GameModel, self).__init__()

    def set_controller(self, ctrl):
        pass

    def flap_wings(self):
        print('flap flap')

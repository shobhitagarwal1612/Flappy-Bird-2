from cocos.layer import Layer
from cocos.scene import Scene

from HUD import HUD
from flappy_bird import BackgroundLayer
from gamectrl import GameCtrl
from gamemodel import GameModel

__all__ = ['get_newgame']


class GameView(Layer):

    def __init__(self, model, hud):
        super(GameView, self).__init__()


def get_newgame():
    '''returns the game scene'''
    scene = Scene()

    # model
    model = GameModel()

    # controller
    ctrl = GameCtrl(model)

    # view
    hud = HUD()
    view = GameView(model, hud)

    # set controller in model
    model.set_controller(ctrl)

    # add controller
    scene.add(ctrl, z=1, name="controller")

    # add view
    scene.add(hud, z=3, name="hud")
    scene.add(BackgroundLayer(), z=0, name="background")
    scene.add(view, z=2, name="view")

    return scene

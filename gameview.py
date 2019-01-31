from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from pyglet.gl import glPushMatrix, glPopMatrix

import gameover
from HUD import HUD
from flappy_bird import BackgroundLayer
from gamectrl import GameCtrl
from gamemodel import GameModel

__all__ = ['get_newgame']


class GameView(Layer):

    def __init__(self, model, hud):
        super(GameView, self).__init__()

        width, height = director.get_window_size()

        aspect = width / float(height)

        self.model = model
        self.hud = hud

        self.model.push_handlers(self.on_game_over,
                                 self.on_flap_wings,
                                 self.on_new_level,
                                 )

        self.hud.show_message('GET READY', self.model.start)

    def on_enter(self):
        super(GameView, self).on_enter()

    def on_exit(self):
        super(GameView, self).on_exit()

    def on_new_level(self):
        pass

    def on_game_over(self):
        self.parent.add(gameover.GameOver(win=False), z=10)
        return True

    def on_flap_wings(self):
        pass

    def draw(self):
        """draw the birdy and pipes"""

        glPushMatrix()
        self.transform()

        glPopMatrix()


def get_newgame():
    """returns the game scene"""

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

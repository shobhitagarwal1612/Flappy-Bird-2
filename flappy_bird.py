import cocos
import pyglet
from cocos.director import director
from cocos.layer import MultiplexLayer, ColorLayer
from cocos.menu import Menu, CENTER, MenuItem, shake, shake_back
from cocos.scene import Scene
from pyglet import font

import gameview
from layers.floor import FloorLayer


class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        self.font_title['font_name'] = 'Arial'
        self.font_title['font_size'] = 50
        self.font_title['color'] = (255, 255, 255, 255)

        self.font_item['font_name'] = 'Arial',
        self.font_item['color'] = (32, 16, 32, 255)
        self.font_item['font_size'] = 32

        self.font_item_selected['font_name'] = 'Arial'
        self.font_item_selected['color'] = (32, 16, 32, 255)
        self.font_item_selected['font_size'] = 46

        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER

        items = [
            MenuItem('New Game', self.on_new_game),
            MenuItem('Options', self.on_options),
            MenuItem('Scores', self.on_scores),
            MenuItem('Quit', self.on_quit)
        ]

        self.create_menu(items, shake(), shake_back())

    def on_new_game(self):
        director.push(gameview.get_newgame())

    def on_options(self):
        self.parent.switch_to(1)

    def on_scores(self):
        self.parent.switch_to(2)

    def on_quit(self):
        pyglet.app.exit()


class OptionsMenu(Menu):

    def __init__(self):
        super(OptionsMenu, self).__init__()


class ScoresLayer(Menu):

    def __init__(self):
        super(ScoresLayer, self).__init__()


class BackgroundLayer(ColorLayer):
    def __init__(self):
        super(BackgroundLayer, self).__init__(0, 0, 0, 255)

        self.background_sprite = cocos.sprite.Sprite(pyglet.resource.image('main_background.png'))
        self.background_sprite.position = self.width / 2, self.height / 2
        self.add(self.background_sprite, z=0)

        self.name_sprite = cocos.sprite.Sprite(pyglet.resource.image('game_name.png'))
        self.name_sprite.position = self.width / 2, self.height * 0.8
        self.add(self.name_sprite, z=20)

        self.floor_layer = FloorLayer(self.width)
        self.floor_layer.position = 0, 50
        self.add(self.floor_layer, z=10)


if __name__ == "__main__":
    pyglet.resource.path.append('res')
    pyglet.resource.reindex()
    font.add_directory('res')

    director.init(resizable=True, width=500, height=800)

    scene = Scene()
    scene.add(MultiplexLayer(MainMenu(), OptionsMenu(), ScoresLayer()), z=1)

    scene.add(BackgroundLayer(), z=0)
    # scene.add(MainLayer())

    director.run(scene)

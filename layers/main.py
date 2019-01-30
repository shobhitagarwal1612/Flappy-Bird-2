import cocos

from layers.bird import BirdLayer
from layers.floor import FloorLayer


class MainLayer(cocos.layer.ColorLayer):

    def __init__(self):
        super(MainLayer, self).__init__(0, 0, 0, 255)

        self.bird_startX = self.width / 2
        self.z_index_bird = 100

        background_sprite = cocos.sprite.Sprite('res/main_background.png')
        background_sprite.position = self.width / 2, self.height / 2
        self.add(background_sprite, z=0)

        name_sprite = cocos.sprite.Sprite('res/game_name.png')
        name_sprite.position = self.width / 2, self.height / 2 + 150
        self.add(name_sprite, z=20)

        play_button_sprite = cocos.sprite.Sprite('res/play_button.png')
        play_button_sprite.position = self.width / 2, self.height / 4
        self.add(play_button_sprite, z=15)

        self.floor_layer = FloorLayer(self.width)
        self.add(self.floor_layer, z=10)

        self.bird_layer = BirdLayer(self.width)
        self.bird_layer.x = self.bird_startX
        self.bird_layer.y = self.height / 2
        self.bird_layer.anchor = 0, 0
        self.bird_layer.ttopOfScreen = self.height
        self.bird_layer.reset()
        self.add(self.bird_layer, z=self.z_index_bird)

    def on_enter(self):
        super(MainLayer, self).on_enter()

        self.floor_layer.start_animation()

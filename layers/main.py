import cocos

from layers.floor import FloorLayer


class MainLayer(cocos.layer.ColorLayer):

    def __init__(self):
        super(MainLayer, self).__init__(0, 0, 0, 255)

        background_sprite = cocos.sprite.Sprite('res/main_background.png')
        background_sprite.position = self.width / 2, self.height / 2
        self.add(background_sprite, z=0)

        name_sprite = cocos.sprite.Sprite('res/game_name.png')
        name_sprite.position = self.width / 2, self.height / 2 + 150
        self.add(name_sprite, z=20)

        play_button_sprite = cocos.sprite.Sprite('res/play_button.png')
        play_button_sprite.position = self.width / 2, self.height / 2 - 150
        self.add(play_button_sprite, z=15)

        floor_layer = FloorLayer()
        self.add(floor_layer, z=10)

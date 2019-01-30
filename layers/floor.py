import cocos


class FloorLayer(cocos.layer.Layer):

    def __init__(self):
        super(FloorLayer, self).__init__()

        self.road_sprite1 = cocos.sprite.Sprite('res/road_base.png')
        self.road_sprite2 = cocos.sprite.Sprite('res/road_base.png')

        self.reset_position()

        self.add(self.road_sprite1)
        self.add(self.road_sprite2)

    def reset_position(self):
        self.road_sprite1.stop()
        self.road_sprite2.stop()

        self.road_sprite1.position = 0, 0
        self.road_sprite1.anchor = 0, 0

        self.road_sprite2.position = self.road_sprite1.width, 0
        self.road_sprite2.anchor = 0, 0

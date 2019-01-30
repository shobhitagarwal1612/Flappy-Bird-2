import cocos


class BirdLayer(cocos.layer.Layer):

    def __init__(self, screen_width):
        super(BirdLayer, self).__init__()

        self.bird_state_moving = 1
        self.bird_state_stopped = 0
        self.bird_start_speedY = 300

        self.screen_width = screen_width

        self.bird_sprite = cocos.sprite.Sprite('res/bird1.png')

        self.add(self.bird_sprite)

    def reset(self):
        self.state = self.bird_state_stopped
        self.set_start_speed()

    def set_start_speed(self):
        self.speedY = self.bird_start_speedY

import cocos


class BirdLayer(cocos.layer.Layer):

    def __init__(self, screen_width):
        super(BirdLayer, self).__init__()

        self.bird_state_moving = 1
        self.bird_state_stopped = 0
        self.bird_start_speedY = 300

        self.screen_width = screen_width

        self.start_flapping()

    def start_flapping(self):
        anim_frames = []

        self.sprite_sheet = cocos.sprite.BatchableNode()
        self.add(self.sprite_sheet)

        # self.sprite1 = cocos.sprite.Sprite("res/bird1.png")
        # self.sprite_sheet.add(self.sprite1)
        #
        self.sprite2 = cocos.sprite.Sprite("res/bird2.png")
        self.sprite_sheet.add(self.sprite2)
        #
        # self.sprite3 = cocos.sprite.Sprite("res/bird3.png")
        # self.sprite_sheet.add(self.sprite3)

    def reset(self):
        self.state = self.bird_state_stopped
        self.set_start_speed()

    def set_start_speed(self):
        self.speedY = self.bird_start_speedY

    def start_vertical_movement(self):
        print('bird vertical movement start')

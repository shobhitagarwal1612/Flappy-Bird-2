import cocos
import cocos.euclid as eu
import pyglet
from cocos.director import director


class Bird(object):

    def __init__(self):
        super(Bird, self).__init__()

        width, height = director.get_window_size()

        self.image = pyglet.resource.image('bird1.png')
        self.top_of_screen = height
        self.gravity = -30000
        self.speedY = 0.0
        self.pos = eu.Point2(width / 2 - 30, height / 2)
        self.radius = 2
        self.rot = 0

    def flap_flap(self):
        self.set_initial_speed()

    def draw(self):
        self.image.blit(self.pos.x, self.pos.y)

    def update_pos(self, dt):
        print(dt)

        distance = self.speedY * dt + 0.5 * self.gravity * dt * dt

        speed = self.speedY + self.gravity * dt

        print('distance = ' + str(distance), 'speed = ' + str(speed))

        self.pos.y = self.pos.y + distance
        self.speedY = speed

        if self.pos.y > self.top_of_screen:
            self.pos.y = self.top_of_screen
            self.speedY = 0.0

    def set_initial_speed(self):
        self.speedY = 2000


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

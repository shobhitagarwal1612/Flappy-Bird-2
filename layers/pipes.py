import cocos.collision_model as cm
import cocos.euclid as eu
import pyglet
from cocos.director import director


class Pipes(object):

    def __init__(self):
        super(Pipes, self).__init__()

        self.winow_width, self.window_height = director.get_window_size()

        self.image = pyglet.resource.image('pipe.png')
        self.speedX = -100
        self.pos = eu.Point2(self.winow_width + self.image.width, self.window_height / 2)
        self.cshape = cm.CircleShape(eu.Vector2(self.pos.x, self.pos.y), self.image.width)

    def draw(self):
        self.image.blit(self.pos.x, self.pos.y)

    def update_pos(self, dt):
        distance = dt * self.speedX
        self.pos.x += distance
        self.cshape = cm.CircleShape(eu.Vector2(self.pos.x, self.pos.y), self.image.width)

    def is_out_of_left_boundary(self):
        return self.pos.x < -self.image.width

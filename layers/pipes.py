import pyglet
from cocos import euclid
from cocos.director import director


class Pipes(object):

    def __init__(self):
        super(Pipes, self).__init__()

        width, height = director.get_window_size()

        self.image = pyglet.resource.image('pipe.png')
        self.top_of_screen = height
        self.speedX = -100
        self.pos = euclid.Point2(width - 50, height / 2)

    def draw(self):
        self.image.blit(self.pos.x, self.pos.y)

    def update_pos(self, dt):
        distance = dt * self.speedX
        self.pos.x += distance

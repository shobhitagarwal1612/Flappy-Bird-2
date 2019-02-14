import weakref

import cocos.collision_model as cm
from cocos.director import director
from pyglet.event import EventDispatcher

import levels
from layers.bird import Bird
from layers.pipes import Pipes
from status import status

__all__ = ['GameModel']


#
# Model (of the MVC pattern)
#

class GameModel(EventDispatcher):

    def __init__(self):
        super(GameModel, self).__init__()

        self.bird = None
        self.pipes = list()

        self.width, self.height = director.get_window_size()

        status.reset()

        status.level = levels.levels[0]

    def set_controller(self, ctrl):
        self.ctrl = weakref.ref(ctrl)

    def flap_wings(self):
        self.bird.flap_flap()

    def start(self):
        self.set_next_level()

    def set_next_level(self):
        self.ctrl().resume_controller()

        if status.level_idx is None:
            status.level_idx = 0
        else:
            status.level_idx += 1

        l = levels.levels[status.level_idx]

        self.init()
        status.level = l()

        self.get_random_pipe()

        self.dispatch_event("on_new_level")

    def move_pipes(self, dt):
        for pipe in self.pipes:
            if pipe.is_out_of_left_boundary():
                self.pipes.remove(pipe)
                print('removing pipe')
            else:
                pipe.update_pos(dt)

    def init(self):
        self.bird = Bird()
        self.bird.set_initial_speed()

        self.collision_manager = cm.CollisionManagerGrid(0, self.width,
                                                         0, self.height,
                                                         self.bird.image.width, self.bird.image.width)

    def get_random_pipe(self):
        pipe = Pipes()
        self.pipes.append(pipe)

        self.collision_manager.add(pipe)
        print('adding pipe')

    def check_collision(self):
        self.collision_manager.clear()
        self.collision_manager.add(self.bird)

        for pipe in self.pipes:
            self.collision_manager.add(pipe)

        print(len(self.collision_manager.known_objs()))

        # interaction - bird and pipes
        for other in self.collision_manager.iter_colliding(self.bird):
            print('other', other)


GameModel.register_event_type('on_new_level')
GameModel.register_event_type('on_game_over')
GameModel.register_event_type('on_flap_wings')

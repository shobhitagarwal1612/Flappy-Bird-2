import cocos
from cocos.actions import MoveTo
from cocos.euclid import Point2


class FloorLayer(cocos.layer.Layer):

    def __init__(self, screen_width):
        super(FloorLayer, self).__init__()

        self.screen_width = screen_width

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

    def start_animation(self):
        # self.schedule_interval(self.keep_moving(), self.get_time() * 3)
        pass

    def keep_moving(self):
        self.reset_position()

        self.move_from_left_corner_to_out_of_screen(self.road_sprite1)
        self.move_from_corner_right_to_center(self.road_sprite2)

    def move_from_left_corner_to_out_of_screen(self, sprite):
        destination = Point2(-sprite.width, 0)
        action_move = MoveTo(destination, self.get_time() * 3)
        # sprite.do(sequence(action_move, CallFunc(self.keep_going())))
        sprite.do(action_move)

    def move_from_corner_right_to_center(self, sprite):
        destination = Point2(0, 0)
        action_move = MoveTo(destination, self.get_time() * 3)
        sprite.do(action_move)

    def get_time(self, pipe_speed=150.0):
        return self.screen_width / pipe_speed

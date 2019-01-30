import cocos
from cocos.sprite import Sprite

from layers.bird import BirdLayer
from layers.floor import FloorLayer
from layers.result_board import ResultLayer


class MainLayer(cocos.layer.ColorLayer):

    def __init__(self):
        super(MainLayer, self).__init__(0, 0, 0, 255)

        self.pipeTypeUpper = 0
        self.pipeTypeLower = 1
        self.pipeTypePair = 2
        self.pipeTypeNone = 3

        self.z_index_bird = 100
        self.bird_startX = self.width / 2

        self._gameTime = 0
        self._gameStarted = False
        self._middleY = self.height / 2
        self._processTouch = False

        self._lastSpawnTime = 0
        self._nextSpawnTime = 0

        self._lastPipeType = self.pipeTypeNone
        self._lastGetUnderY = 0

        self._score = 0
        self._highScore = 0

        self.background_sprite = cocos.sprite.Sprite('res/main_background.png')
        self.background_sprite.position = self.width / 2, self.height / 2
        self.add(self.background_sprite, z=0)

        self.name_sprite = cocos.sprite.Sprite('res/game_name.png')
        self.name_sprite.position = self.width / 2, self.height / 2 + 150
        self.add(self.name_sprite, z=20)

        self.play_button_sprite = cocos.sprite.Sprite('res/play_button.png')
        self.play_button_sprite.position = self.width / 2, self.height / 4
        self.add(self.play_button_sprite, z=15)

        self._gameReadyLabel = Sprite('res/get_ready.png')
        self._gameReadyLabel.x = self.width / 2
        self._gameReadyLabel.y = self.height / 2 * 1.5
        self._gameReadyLabel.visible = False
        self.add(self._gameReadyLabel, self.z_index_bird)

        self._tapTapLabel = Sprite('res/tap_tap.png')
        self._tapTapLabel.x = self.width / 2 + 50
        self._tapTapLabel.y = self.height / 2
        self._tapTapLabel.visible = False
        self.add(self._tapTapLabel, self.z_index_bird)

        self._gameOverLabel = Sprite('res/game_over.png')
        self._gameOverLabel.x = self.width / 2
        self._gameOverLabel.y = self.height / 2 * 1.5
        self._gameOverLabel.visible = False
        self.add(self._gameOverLabel, self.z_index_bird)

        self._resultBoard = ResultLayer()
        self._resultBoard.x = self.width / 2
        self._resultBoard.y = self.height / 2 + 50
        self._resultBoard.visible = False
        self.add(self._resultBoard, self.z_index_bird)

        self._scoreLabel = cocos.text.Label(
            '0',
            font_name='res/FlappyBirdy.ttf',
            font_size=32
        )

        self._scoreLabel.position = self.width / 2, self.height - 100
        self._scoreLabel.anchor = 0, 1
        self._scoreLabel.visible = False
        self.add(self._scoreLabel, self.z_index_bird)

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

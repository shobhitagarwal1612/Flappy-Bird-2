import cocos
from cocos.sprite import Sprite


class ResultLayer(cocos.layer.Layer):

    def __init__(self):
        super(ResultLayer, self).__init__()

        self._result_board = Sprite('res/result_board.png')

        self._medal_silver = Sprite('res/medal_silver.png')
        self._medal_silver.x = -105
        self._medal_silver.y = -15
        self.add(self._medal_silver, 1)

        self._medal_gold = Sprite('res/medal_gold.png')
        self._medal_gold.x = -105
        self._medal_gold.y = -15
        self.add(self._medal_gold, 1)

        self._scoreLabel = cocos.text.Label(
            '0',
            font_name='res/FlappyBirdy.ttf',
            font_size=32
        )
        self._scoreLabel.position = 120, 22
        self.add(self._scoreLabel, z=2)

        self._highScoreLabel = cocos.text.Label(
            '0',
            font_name='res/FlappyBirdy.ttf',
            font_size=32
        )
        self._highScoreLabel.position = 120, -45
        self.add(self._highScoreLabel, z=2)

        self.add(self._result_board, 0)

    def set_score(self, score, highscore):
        self._medal_silver.visible = False
        self._medal_gold.visible = False

        if score >= 50:
            self._medal_gold.visible = True
        elif score >= 20:
            self._medal_silver.visible = True

        self._scoreLabel.string = score
        self._highScoreLabel.string = highscore

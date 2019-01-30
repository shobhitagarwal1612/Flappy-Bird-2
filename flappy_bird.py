import cocos
from cocos.director import director

from layers.main import MainLayer

director.init(resizable=True)

director.run(cocos.scene.Scene(MainLayer()))

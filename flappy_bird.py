import pyglet
from cocos.director import director
from cocos.scene import Scene
from pyglet import font

from layers.main import MainLayer

if __name__ == "__main__":
    pyglet.resource.path.append('res')
    pyglet.resource.reindex()
    font.add_directory('res')

    director.init(resizable=True, width=600, height=720)

    scene = Scene()
    scene.add(MainLayer(), z=0)

    director.run(scene)

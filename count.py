from pico2d import *

import game_framework
import game_world


class Three:
    image = None

    def __init__(self):
        if Three.image is None:
            Three.image = load_image("image/3.png")

        self.x, self.y = 400, 300

    def draw(self):
        self.image.clip_draw(0, 0, 60, 60, self.x, self.y)

    def update(self):
        pass


class Two:
    image = None

    def __init__(self):
        if Two.image is None:
            Two.image = load_image('image/2.png')

        self.x, self.y = 400, 300

    def draw(self):
        self.image.clip_draw(0, 0, 60, 60, self.x, self.y)

    def update(self):
        pass


class One:
    image = None
    fromwhere = 0

    def __init__(self):
        if One.image is None:
            One.image = load_image('image/1.png')

        self.x, self.y = 400, 300

    def draw(self):
        self.image.clip_draw(0, 0, 60, 60, self.x, self.y)

    def update(self):
        pass

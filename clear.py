from pico2d import *

class Clear:
    image = None

    def __init__(self):
        if Clear.image is None:
            Clear.image = load_image("image/Clear.png")

    def draw(self):
        self.image.clip_draw(0, 0, 353, 131, 400, 300)

    def update(self):
        pass
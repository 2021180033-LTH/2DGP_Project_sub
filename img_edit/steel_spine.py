from pico2d import *


class Spine:
    image = None

    def __init__(self):
        if Spine.image is None:
            Spine.image = load_image('image/steel_spine.png')

        self.x_spi, self.y_spi = 0, 0
        self.ifhit = 0

    def draw(self):
        self.image.clip_draw(0, 0, 30, 32, self.x_spi, self.y_spi)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x_spi - 15, self.y_spi - 16, self.x_spi + 15, self.y_spi + 16

    def handle_collision(self, other, group):
        if group == 'ball:spine':
            self.ifhit = 1

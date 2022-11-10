from pico2d import *


class Spine:
    def __init__(self):
        self.spi1 = load_image("steel_spine.png")
        self.spi2 = load_image("steel_spine.png")
        self.spi3 = load_image("steel_spine.png")
        self.spi4 = load_image("steel_spine.png")
        self.spi5 = load_image("steel_spine.png")

        self.x_spi1, self.y_spi1 = 140, 469
        self.x_spi2, self.y_spi2 = 172, 439
        self.x_spi3, self.y_spi3 = 478, 375
        self.x_spi4, self.y_spi4 = 508, 352

    def draw(self):
        self.spi1.clip_draw(0, 0, 30, 31, self.x_spi1, self.y_spi1)
        self.spi2.clip_draw(0, 0, 30, 31, self.x_spi2, self.y_spi2)
        self.spi3.clip_draw(0, 0, 30, 31, self.x_spi3, self.y_spi3)
        self.spi4.clip_draw(0, 0, 30, 31, self.x_spi4, self.y_spi4)

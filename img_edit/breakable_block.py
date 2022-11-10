from pico2d import *


class Bb:
    def __init__(self):
        self.bbl1 = load_image("breakable_block.png")
        self.bbl2 = load_image("breakable_block.png")
        self.bbl3 = load_image("breakable_block.png")

        self.x_bbl1, self.y_bbl1 = 490, 200
        self.x_bbl2, self.y_bbl2 = 525, 75
        self.x_bbl3, self.y_bbl3 = 610, 50

    def draw(self):
        self.bbl1.clip_draw(0, 0, 32, 32, self.x_bbl1, self.y_bbl1)
        self.bbl2.clip_draw(0, 0, 32, 32, self.x_bbl2, self.y_bbl2)
        self.bbl3.clip_draw(0, 0, 32, 32, self.x_bbl3, self.y_bbl3)

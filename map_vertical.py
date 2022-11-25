from pico2d import *
import game_framework


class Wall:
    def __init__(self):
        self.image = load_image("vertical_steel_block.png")
        self.x, self.y = 138, 253
        self.gap = 32

    def draw(self):
        self.image.clip_draw(0, 0, 25, 120, self.x, self.y)
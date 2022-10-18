from pico2d import *
import game_framework


class Wall:
    def __init__(self):
        self.image = load_image("vertex_steel_block.png")
        self.x, self.y = 400, 180
        self.gap = 32

    def draw(self):
        self.image.clip_draw(0, 0, 550, 25, self.x, self.y)

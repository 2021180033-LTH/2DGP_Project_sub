from pico2d import *


class Map3:
    def __init__(self):
        self.hor1 = load_image("image/half_vertex_steel_block.png")
        self.hor2 = load_image("image/quarter_vertex_steel_block.png")
        self.hor3 = load_image("image/quarter_vertex_steel_block.png")
        self.hor4 = load_image("image/half_vertex_steel_block.png")
        self.hor5 = load_image("image/half_vertex_steel_block.png")

        self.ver1 = load_image("image/vertical_steel_block.png")
        self.ver2 = load_image("image/vertical_steel_block.png")

        self.x_hz1, self.y_hz1 = 326, 400
        self.x_hz2, self.y_hz2 = 63, 467
        self.x_hz3, self.y_hz3 = 739, 10
        self.x_hz4, self.y_hz4 = 665, 250
        self.x_hz5, self.y_hz5 = 325, 125

        self.x_vt1, self.y_vt1 = 13, 540
        self.x_vt2, self.y_vt2 = 790, 83

    def draw(self):
        self.hor1.clip_draw(0, 0, 275, 25, self.x_hz1, self.y_hz1)
        self.hor2.clip_draw(0, 0, 125, 25, self.x_hz2, self.y_hz2)
        self.hor3.clip_draw(0, 0, 125, 25, self.x_hz3, self.y_hz3)
        self.hor4.clip_draw(0, 0, 275, 25, self.x_hz4, self.y_hz4)
        self.hor5.clip_draw(0, 0, 275, 25, self.x_hz5, self.y_hz5)

        self.ver1.clip_draw(0, 0, 25, 120, self.x_vt1, self.y_vt1)
        self.ver2.clip_draw(0, 0, 25, 120, self.x_vt2, self.y_vt2)

    def update(self):
        pass
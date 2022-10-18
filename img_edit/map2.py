from pico2d import *


class Map2:
    def __init__(self):
        self.image1 = load_image("half_vertex_steel_block.png")
        self.image2 = load_image("quarter_vertex_steel_block.png")
        self.image3 = load_image("quarter_vertex_steel_block.png")
        self.image4 = load_image("vertical_steel_block.png")
        self.image5 = load_image("vertical_steel_block.png")
        self.image6 = load_image("star.png")
        self.x_hz1, self.y_hz1 = 400, 304
        self.x_hz2, self.y_hz2 = 200, 327
        self.x_hz3 = 600
        self.x_vt1, self.y_vt = 150, 400
        self.x_vt2 = 650
        self.x_st, self.y_st = 620, 360
        self.gap = 32

    def draw(self):
        self.image1.clip_draw(0, 0, 275, 25, self.x_hz1, self.y_hz1)
        self.image2.clip_draw(0, 0, 125, 25, self.x_hz2, self.y_hz2)
        self.image3.clip_draw(0, 0, 125, 25, self.x_hz3, self.y_hz2)
        self.image4.clip_draw(0, 0, 25, 120, self.x_vt1, self.y_vt)
        self.image5.clip_draw(0, 0, 25, 120, self.x_vt2, self.y_vt)
        self.image6.clip_draw(0, 0, 32, 32, self.x_st, self.y_st)
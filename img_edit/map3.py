from pico2d import *


class Map3:
    def __init__(self):
        self.hor1 = load_image("half_vertex_steel_block.png")
        self.hor2 = load_image("quarter_vertex_steel_block.png")
        self.hor3 = load_image("quarter_vertex_steel_block.png")
        self.hor4 = load_image("half_vertex_steel_block.png")
        self.hor5 = load_image("half_vertex_steel_block.png")

        self.ver1 = load_image("vertical_steel_block.png")
        self.ver2 = load_image("vertical_steel_block.png")

        self.star1 = load_image("star.png")
        self.star2 = load_image("star.png")
        self.star3 = load_image("star.png")
        self.star4 = load_image("star.png")

        self.spi1 = load_image("steel_spine.png")
        self.spi2 = load_image("steel_spine.png")
        self.spi3 = load_image("steel_spine.png")
        self.spi4 = load_image("steel_spine.png")
        self.spi5 = load_image("steel_spine.png")

        self.bbl1 = load_image("breakable_block.png")
        self.bbl2 = load_image("breakable_block.png")
        self.bbl3 = load_image("breakable_block.png")

        self.x_hz1, self.y_hz1 = 326, 400
        self.x_hz2, self.y_hz2 = 63, 467
        self.x_hz3, self.y_hz3 = 739, 10
        self.x_hz4, self.y_hz4 = 665, 250
        self.x_hz5, self.y_hz5 = 325, 125

        self.x_vt1, self.y_vt1 = 13, 540
        self.x_vt2, self.y_vt2 = 790, 83

        self.x_st1, self.y_st1 = 325, 430
        self.x_st2, self.y_st2 = 760, 280
        self.x_st3, self.y_st3 = 325, 155
        self.x_st4, self.y_st4 = 750, 50

        self.x_spi1, self.y_spi1 = 140, 469
        self.x_spi2, self.y_spi2 = 172, 439
        self.x_spi3, self.y_spi3 = 478, 375
        self.x_spi4, self.y_spi4 = 508, 352

        self.x_bbl1, self.y_bbl1 = 490, 200
        self.x_bbl2, self.y_bbl2 = 525, 75
        self.x_bbl3, self.y_bbl3 = 610, 50

        self.gap = 32

    def draw(self):
        self.hor1.clip_draw(0, 0, 275, 25, self.x_hz1, self.y_hz1)
        self.hor2.clip_draw(0, 0, 125, 25, self.x_hz2, self.y_hz2)
        self.hor3.clip_draw(0, 0, 125, 25, self.x_hz3, self.y_hz3)
        self.hor4.clip_draw(0, 0, 275, 25, self.x_hz4, self.y_hz4)
        self.hor5.clip_draw(0, 0, 275, 25, self.x_hz5, self.y_hz5)

        self.ver1.clip_draw(0, 0, 25, 120, self.x_vt1, self.y_vt1)
        self.ver2.clip_draw(0, 0, 25, 120, self.x_vt2, self.y_vt2)

        self.star1.clip_draw(0, 0, 32, 32, self.x_st1, self.y_st1)
        self.star2.clip_draw(0, 0, 32, 32, self.x_st2, self.y_st2)
        self.star3.clip_draw(0, 0, 32, 32, self.x_st3, self.y_st3)
        self.star4.clip_draw(0, 0, 32, 32, self.x_st4, self.y_st4)

        self.spi1.clip_draw(0, 0, 30, 31, self.x_spi1, self.y_spi1)
        self.spi2.clip_draw(0, 0, 30, 31, self.x_spi2, self.y_spi2)
        self.spi3.clip_draw(0, 0, 30, 31, self.x_spi3, self.y_spi3)
        self.spi4.clip_draw(0, 0, 30, 31, self.x_spi4, self.y_spi4)

        self.bbl1.clip_draw(0, 0, 32, 32, self.x_bbl1, self.y_bbl1)
        self.bbl2.clip_draw(0, 0, 32, 32, self.x_bbl2, self.y_bbl2)
        self.bbl3.clip_draw(0, 0, 32, 32, self.x_bbl3, self.y_bbl3)
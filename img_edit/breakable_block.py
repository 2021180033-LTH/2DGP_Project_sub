from pico2d import *
import game_world


class Bb:
    image = None
    def __init__(self):
        if Bb.image is None:
            Bb.image = load_image("image/breakable_block.png")

        self.x_bbl, self.y_bbl = 0, 0

    def draw(self):
        self.image.clip_draw(0, 0, 32, 32, self.x_bbl, self.y_bbl)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x_bbl - 16, self.y_bbl - 16, self.x_bbl + 16, self.y_bbl + 16

    def handle_collision(self, other, group):
        if group == 'ball:bbl':
            game_world.remove_object(self)

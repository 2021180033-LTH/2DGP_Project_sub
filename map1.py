from pico2d import *


class Vertex:
    image = None

    def __init__(self):
        self.image1 = load_image("image/vertex_steel_block.png")

        self.x, self.y = 400, 180

    def draw(self):
        self.image1.clip_draw(0, 0, 550, 25, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 275, self.y - 13, self.x + 275, self.y + 13

    def handle_collision(self, other, group):
        if group == 'ball:ground':
            pass


class Vertical:
    image = None

    def __init__(self):
        if Vertical.image is None:
            Vertical.image = load_image('image/vertical_steel_block.png')

        self.x, self.y = 0, 0

    def draw(self):
        self.image.clip_draw(0, 0, 25, 120, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 13, self.y - 60, self.x + 13, self.y + 60

    def handle_collision(self, other, group):
        if group == 'ball:wall':
            pass

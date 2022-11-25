from pico2d import *


class Vertex_h:
    image = None

    def __init__(self):
        if Vertex_h.image is None:
            Vertex_h.image = load_image('image/half_vertex_steel_block.png')
        self.x, self.y = 0, 0

    def draw(self):
        self.image.clip_draw(0, 0, 275, 25, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 137.5, self.y - 12.5, self.x + 137.5, self.y + 12.5

    def handle_collision(self, other, group):
        if group == 'ball:ground':
            pass


class Vertex_q:
    image = None

    def __init__(self):
        if Vertex_q.image is None:
            Vertex_q.image = load_image('image/quarter_vertex_steel_block.png')
        self.x, self.y = 0, 0

    def draw(self):
        self.image.clip_draw(0, 0, 125, 25, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 62.5, self.y - 12.5, self.x + 62.5, self.y + 12.5

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
        return self.x - 12.5, self.y - 60, self.x + 12.5, self.y + 60

    def handle_collision(self, other, group):
        if group == 'ball:wall':
            pass

from pico2d import *


class Vertex:
    image = None
    sound = None

    def __init__(self):
        if Vertex.image is None:
            Vertex.image = load_image("image/vertex_steel_block.png")

        if Vertex.sound is None:
            Vertex.sound = load_music('sound/normalCollision')
            Vertex.sound.get_volume(16)
        self.x, self.y = 400, 180

    def draw(self):
        self.image1.clip_draw(0, 0, 550, 25, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 275, self.y - 13, self.x + 275, self.y + 13

    def handle_collision(self, other, group):
        if group == 'ball:ground_f':
            self.sound.play()

class Vertex_h:
    image = None
    sound = None

    def __init__(self):
        if Vertex_h.image is None:
            Vertex_h.image = load_image('image/half_vertex_steel_block.png')
        if Vertex_h.sound is None:
            Vertex_h.sound = load_music('sound/normalCollision')
            Vertex_h.sound.get_volume(16)
        self.x, self.y = 0, 0

    def draw(self):
        self.image.clip_draw(0, 0, 275, 25, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 137.5, self.y - 12.5, self.x + 137.5, self.y + 12.5

    def handle_collision(self, other, group):
        if group == 'ball:ground_h':
            self.sound.play()


class Vertex_q:
    image = None
    sound = None

    def __init__(self):
        if Vertex_q.image is None:
            Vertex_q.image = load_image('image/quarter_vertex_steel_block.png')
        if Vertex_q.sound is None:
            Vertex_q.sound = load_music('sound/normalCollision')
            Vertex_q.sound.get_volume(16)
        self.x, self.y = 0, 0

    def draw(self):
        self.image.clip_draw(0, 0, 125, 25, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 62.5, self.y - 12.5, self.x + 62.5, self.y + 12.5

    def handle_collision(self, other, group):
        if group == 'ball:ground_q':
            self.sound.play()


class Vertical:
    image = None
    sound = None

    def __init__(self):
        if Vertical.image is None:
            Vertical.image = load_image('image/vertical_steel_block.png')
        if Vertical.sound is None:
            Vertical.sound = load_music('sound/normalCollision')
            Vertical.sound.get_volume(16)

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
            self.sound.play()

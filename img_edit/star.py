from pico2d import *
import game_world

class Star:
    def __init__(self):
        self.num = 0
        self.image4 = load_image("star.png")

    def draw(self):
        self.image4.clip_draw(0, 0, 32, 32, self.x_st, self.y_st)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x_st - 16, self.y_st - 16, self.x_st + 16, self.y_st + 16

    def handle_collision(self, other, group):
        if group == 'ball:star':
            game_world.remove_object(self)
            self.num += 1


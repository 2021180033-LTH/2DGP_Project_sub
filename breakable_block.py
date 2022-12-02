from pico2d import *
import game_world


class Bb:
    image = None
    def __init__(self):
        if Bb.image is None:
            Bb.image = load_image("image/breakable_block.png")
        if Bb.sound is None:
            Bb.sound = load_music('sound/pang.wav')
            Bb.sound.set_volume(16)
        self.x, self.y = 0, 0

    def draw(self):
        self.image.clip_draw(0, 0, 32, 32, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

    def handle_collision(self, other, group):
        if group == 'ball:bbl':
            game_world.remove_collision_object(self)
            game_world.remove_object(self)
            self.sound.play()

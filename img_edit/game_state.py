from pico2d import *
import game_framework
import map1
import map2

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Ball:
    def __init__(self):
        self.image = load_image("ball.png")
        self.x, self.y = 165, 200  # map1 xy
        # self.x, self.y = 170, 346 map2 xy
        self.frame = 0
        self.isJump = 0
        self.jump_progress_v, self.jump_g = 12, 1
        self.jump_last_v = -12
        self.jump_y = self.y

    def update(self):
        global dirx, diry
        self.x += dirx * 1.5
        if self.x > 800:
            self.x = 800
        elif self.x < 0:
            self.x = 0

        if self.isJump > 0:
            self.y += self.jump_progress_v
            self.jump_progress_v = self.jump_progress_v - self.jump_g

            if self.jump_last_v - 1 == self.jump_progress_v:
                self.jump(0)
                self.jump_progress_v = 12
        delay(0.015)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 25, 25, self.x, self.y)

    def jump(self, j):
        self.isJump = j


def handle_events():
    global running
    global dirx

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = quit()
            elif event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                if ball.isJump == 0:
                    ball.jump(1)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1


running = True
ball = None
first_map = None
second_map = None
gr = 11
dirx, diry, VELOCITY, MASS = 0, 0, 5, 5


def enter():
    global ball, running, first_map, second_map
    ball = Ball()
    first_map = map1.Map1()
    second_map = map2.Map2()
    running = True


def exit():
    global ball, first_map, second_map
    del ball, first_map, second_map


def update():
    ball.update()


def draw_world():
    ball.draw()
    first_map.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()

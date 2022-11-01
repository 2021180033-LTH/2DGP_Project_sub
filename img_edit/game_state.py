from pico2d import *
import game_framework
import map1
import map2
from ball import Ball

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

running = True
ball = None
first_map = None
second_map = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            ball.handle_event(event)


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
    # first_map.draw()
    second_map.draw()


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

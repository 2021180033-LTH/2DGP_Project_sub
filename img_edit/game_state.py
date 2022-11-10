from pico2d import *
import game_framework
import game_world
from map1 import Map1
from map2 import Map2
from map3 import Map3
from ball import Ball
from star import Star

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

running = True
ball = None
first_map = None
second_map = None
third_map = None
star = None


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
    global ball, running, first_map, second_map, third_map, star
    ball = Ball()
    first_map = Map1()
    second_map = Map2()
    third_map = Map3()
    star = Star()
    running = True
    game_world.add_object(first_map, 0)
    game_world.add_object(ball, 1)
    game_world.add_object(star, 1)

    game_world.add_collision_group(ball, star, 'ball:star')


def exit():
    # global ball, first_map, second_map, third_map
    # del ball, first_map, second_map, third_map
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()

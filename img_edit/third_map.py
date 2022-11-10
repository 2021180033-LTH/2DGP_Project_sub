from pico2d import *
import game_framework
import game_world
import title_state

from map3 import Map3
from ball import Ball
from star import Star
from steel_spine import Spine
from breakable_block import Bb

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

running = True
ball = None
third_map = None
stars = []
spines = []
bbls = []


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif stars[3].num == 1:
            game_framework.change_state(title_state)
        else:
            ball.handle_event(event)


def enter():
    global ball, running, third_map, stars, spines, bbls
    ball = Ball()
    ball.x, ball.y = 50, 490
    third_map = Map3()

    spines = [Spine() for i in range(5)]
    spines[0].x_spi, spines[0].y_spi = 140, 469
    spines[1].x_spi, spines[1].y_spi = 172, 439
    spines[2].x_spi, spines[2].y_spi = 478, 375
    spines[3].x_spi, spines[3].y_spi = 508, 352

    stars = [Star() for i in range(4)]
    stars[0].x_st, stars[0].y_st = 325, 430
    stars[1].x_st, stars[1].y_st = 760, 280
    stars[2].x_st, stars[2].y_st = 325, 155
    stars[3].x_st, stars[3].y_st = 750, 50

    bbls = [Bb() for i in range(4)]
    bbls[0].x_bbl, bbls[0].y_bbl = 490, 200
    bbls[1].x_bbl, bbls[1].y_bbl = 525, 75
    bbls[2].x_bbl, bbls[2].y_bbl = 610, 50

    running = True
    game_world.add_object(third_map, 0)
    game_world.add_object(ball, 1)
    game_world.add_objects(stars, 1)
    game_world.add_objects(spines, 1)
    game_world.add_objects(bbls, 1)

    game_world.add_collision_group(ball, stars, 'ball:star')
    game_world.add_collision_group(ball, bbls, 'ball:bbl')
    game_world.add_collision_group(ball, spines, 'ball:spine')


def exit():
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
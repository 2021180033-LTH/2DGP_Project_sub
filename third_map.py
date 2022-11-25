from pico2d import *
import game_framework
import game_world
import restart_3
import clear_state_3

from map3 import Vertex_q
from map3 import Vertex_h
from map3 import Vertical
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
vertex_q = []
vertex_h = []
vertical = []


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
    global ball, running, third_map, stars, spines, bbls, vertex_h, vertex_q, vertical
    ball = Ball()
    ball.x, ball.y = 50, 490

    spines = [Spine() for i in range(4)]
    spines[0].x_spi, spines[0].y_spi = 140, 439
    spines[1].x_spi, spines[1].y_spi = 172, 439
    spines[2].x_spi, spines[2].y_spi = 478, 375
    spines[3].x_spi, spines[3].y_spi = 508, 375

    stars = [Star() for i in range(4)]
    stars[0].x_st, stars[0].y_st = 325, 450
    stars[1].x_st, stars[1].y_st = 760, 280
    stars[2].x_st, stars[2].y_st = 325, 155
    stars[3].x_st, stars[3].y_st = 750, 50

    bbls = [Bb() for i in range(4)]
    bbls[0].x, bbls[0].y = 156, 500
    bbls[1].x, bbls[1].y = 493, 413
    bbls[2].x, bbls[2].y = 525, 75
    bbls[3].x, bbls[3].y = 610, 50

    vertex_h = [Vertex_h() for i in range(3)]
    vertex_h[0].x, vertex_h[0].y = 326, 413
    vertex_h[1].x, vertex_h[1].y = 665, 250
    vertex_h[2].x, vertex_h[2].y = 325, 125

    vertex_q = [Vertex_q() for i in range(2)]
    vertex_q[0].x, vertex_q[0].y = 63, 467
    vertex_q[1].x, vertex_q[1].y = 739, 10

    vertical = [Vertical() for i in range(2)]
    vertical[0].x, vertical[0].y = 13, 540
    vertical[1].x, vertical[1].y = 790, 83

    running = True
    game_world.add_object(ball, 1)
    game_world.add_objects(stars, 2)
    game_world.add_objects(spines, 0)
    game_world.add_objects(bbls, 0)
    game_world.add_objects(vertex_h, 0)
    game_world.add_objects(vertex_q, 0)
    game_world.add_objects(vertical, 0)

    game_world.add_collision_group(ball, stars, 'ball:star')
    game_world.add_collision_group(ball, bbls, 'ball:bbl')
    game_world.add_collision_group(ball, spines, 'ball:spine')
    game_world.add_collision_group(ball, vertex_q, 'ball:ground_q')
    game_world.add_collision_group(ball, vertex_h, 'ball:ground_h')
    game_world.add_collision_group(ball, vertical, 'ball:wall')


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if stars[3].num == 1:
        for game_object in game_world.all_objects():
            game_world.remove_collision_object(game_object)
            game_world.remove_object(game_object)
        game_framework.change_state(clear_state_3)

    if spines[0].ifhit or spines[1].ifhit or spines[2].ifhit or spines[3].ifhit:
        for game_object in game_world.all_objects():
            game_world.remove_collision_object(game_object)
            game_world.remove_object(game_object)
        game_framework.change_state(restart_3)

    if ball.x > 800 or ball.x < 0 or ball.y < 0:
        for game_object in game_world.all_objects():
            game_world.remove_collision_object(game_object)
            game_world.remove_object(game_object)
        game_framework.change_state(restart_3)

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
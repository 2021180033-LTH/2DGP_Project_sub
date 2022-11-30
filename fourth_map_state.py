from pico2d import *
import game_framework
import game_world
import restart_3_state
import clear_state
from clear import Clear

from count import One
from map import Vertical
from ball import Ball
from star import Star

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

running = True
ball = None
fourth_map = None
star = []
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
    global ball, running, star, vertical
    ball = Ball()
    ball.x, ball.y = 400, 600

    star = Star()
    star.x_st, star.y_st = 400, 250

    vertical = [Vertical() for i in range(2)]
    vertical[0].x, vertical[0].y = 400, 450
    vertical[1].x, vertical[1].y = 400, 60
    running = True
    game_world.add_object(ball, 1)
    game_world.add_object(star, 2)
    game_world.add_objects(vertical, 0)

    game_world.add_collision_group(ball, star, 'ball:star')
    game_world.add_collision_group(ball, vertical, 'ball:wall')


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if star.get is True:
        for game_object in game_world.all_objects():
            game_world.remove_collision_object(game_object)
        game_world.clear()
        Clear.fromwhere = 4
        game_framework.change_state(clear_state)

    if ball.x > 800 or ball.x < 0 or ball.y < 0:
        for game_object in game_world.all_objects():
            game_world.remove_collision_object(game_object)
        game_world.clear()
        One.fromwhere = 4
        game_framework.change_state(restart_3_state)

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

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()

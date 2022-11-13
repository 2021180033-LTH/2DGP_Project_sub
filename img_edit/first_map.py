from pico2d import *
import game_framework
import game_world
import second_map
from map1 import Vertex
from map1 import Vertical
from ball import Ball
from star import Star

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

running = True
ball = None
vertex = None
vertical = None
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
    global ball, running, vertex, vertical, star

    ball = Ball()
    ball.x, ball.y = 165, 200

    vertex = Vertex()

    vertical = [Vertical() for i in range(2)]
    vertical[0].x, vertical[0].y = 138, 253
    vertical[1].x, vertical[1].y = 661.5, 253

    star = Star()
    star.x_st, star.y_st = 630, 210
    running = True

    game_world.add_object(vertex, 0)
    game_world.add_objects(vertical, 0)
    game_world.add_object(ball, 1)
    game_world.add_object(star, 1)

    game_world.add_collision_group(ball, star, 'ball:star')
    game_world.add_collision_group(ball, vertex, 'ball:ground')
    game_world.add_collision_group(ball, vertical, 'ball:wall')


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if star.num == 1:
        game_framework.change_state(second_map)

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

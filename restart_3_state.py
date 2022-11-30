from pico2d import *
import game_framework
import game_world
from count import Three
import restart_2_state

three = None
two = None
one = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()



def enter():
    global three, two, one

    three = Three()

    game_world.add_object(three, 2)


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    delay(1)
    game_world.clear()
    game_framework.change_state(restart_2_state)


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


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()

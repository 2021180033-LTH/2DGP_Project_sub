from pico2d import *
import game_framework
import game_world
from clear import Clear
import title_state
import second_map_state
import third_map_state
import fourth_map_state

clear = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if Clear.fromwhere == 1:
                game_framework.change_state(second_map_state)
            if Clear.fromwhere == 2:
                game_framework.change_state(third_map_state)
            if Clear.fromwhere == 3:
                game_framework.change_state(fourth_map_state)
            if Clear.fromwhere == 4:
                game_framework.change_state(title_state)


def enter():
    global clear

    clear = Clear()

    game_world.add_object(clear, 0)


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()


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

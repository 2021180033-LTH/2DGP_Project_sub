from pico2d import *
import game_framework
import first_map_state

image = None


def enter():
    global image
    image = load_image('image/title_image.png')
    # fill here
    pass


def exit():
    global image
    del image
    # fill here
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(first_map_state)
    # fill here
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass




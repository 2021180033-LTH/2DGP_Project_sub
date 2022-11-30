from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.1)
RUN_SPEED_KMPH = 0.1
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_PPM = (RUN_SPEED_MPM * PIXEL_PER_METER)

JUMP_SPEED_KMPH = 0.1
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_PPM = (JUMP_SPEED_MPM * PIXEL_PER_METER)

RD, RU, LD, LU, UD, UU, FL = range(7)
event_name = ['RD', 'RU', 'LD', 'LU', 'UD', 'UU']

key_event_table = {(SDL_KEYDOWN, SDLK_RIGHT): RD, (SDL_KEYUP, SDLK_RIGHT): RU,
                   (SDL_KEYDOWN, SDLK_LEFT): LD, (SDL_KEYUP, SDLK_LEFT): LU,
                   (SDL_KEYDOWN, SDLK_UP): UD, (SDL_KEYUP, SDLK_UP): UU}


class IDLE:
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0
        self.isjump = False
        self.on_ground = False

    def exit(self):
        print('EXIT IDLE')

    def do(self):
        if not self.jump:
            pass
        else:
            self.jump_func()
            if self.on_ground:
                self.jump = False
                self.y_velocity = self.jump_height

    def draw(self):
        self.image.clip_draw(0, 0, 25, 25, self.x, self.y)
        draw_rectangle(*self.get_bb())


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        if event == RU:
            self.dir -= 1
        if event == LD:
            self.dir -= 1
        if event == LU:
            self.dir += 1

        self.on_ground = False

    def exit(self):
        print('EXIT RUN')

    def do(self):
        self.x += self.dir * RUN_SPEED_PPM * game_framework.frame_time

        if self.jump:
            self.jump_func()
            if self.on_ground:
                self.jump = False
                self.y_velocity = self.jump_height

    def draw(self):
        self.image.clip_draw(0, 0, 25, 25, self.x, self.y)
        draw_rectangle(*self.get_bb())


# class FALL:
#     def enter(self, event):
#         print('ENTER FALL')
#         if event == RD:
#             self.dir += 1
#         if event == RU:
#             self.dir -= 1
#         if event == LD:
#             self.dir -= 1
#         if event == LU:
#             self.dir += 1
#
#     def exit(self):
#         print('EXIT FALL')
#
#     def do(self):
#         self.frame = 0
#         self.x += self.dir * RUN_SPEED_PPM * game_framework.frame_time
#
#         if not self.on_ground:
#             self.y -= self.y_velocity
#
#     def draw(self):
#         self.image.clip_draw(self.frame * 100, 0, 25, 25, self.x, self.y)
#         draw_rectangle(*self.get_bb())


next_state = {
    IDLE: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, UD: RUN, UU: RUN},
    RUN: {RD: IDLE, RU: IDLE, LD: IDLE, LU: IDLE, UU: RUN, UD: RUN}
}


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('image/ball.png')
        self.x, self.y = 0, 0

        self.jump = False
        self.y_velocity = 2
        self.on_ground = False

        self.mass = 10
        self.jump_height = 4
        self.gravity = 0.05
        self.fall_speed = self.gravity
        self.y_velocity = self.jump_height

        self.event_q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_q:
            event = self.event_q.pop()
            if event == UD:
                self.jump = True
                self.on_ground = False
            self.cur_state.exit(self)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('ERROR:', self.cur_state, event_name[event])
            self.cur_state.enter(self, event)

        if self.on_ground is False and self.jump is False:
            self.fall_func()

    def jump_func(self):
        self.y += self.y_velocity * JUMP_SPEED_PPM * game_framework.frame_time
        self.y_velocity -= self.gravity

    def fall_func(self):
        self.y -= self.fall_speed * JUMP_SPEED_PPM * game_framework.frame_time
        self.fall_speed += self.gravity

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 8, self.y - 8, self.x + 8, self.y + 8

    def handle_collision(self, other, group):
        if group == 'ball:star':
            self.cur_state.enter(IDLE, None)

        if group == 'ball:ground_f':
            self.on_ground = True
            if self.x < other.x - 275:
                self.x = max(other.x - 275, self.x) - 12
            if self.x > other.x + 275:
                self.x = min(other.x + 275, self.x) + 12
            if other.x - 275 <= self.x <= other.x + 275:
                self.y = other.y + 20

        if group == 'ball:ground_h':
            self.on_ground = True
            if self.x < other.x - 137.5:
                self.x = max(other.x - 137.5, self.x) - 12
            if self.x > other.x + 137.5:
                self.x = min(other.x + 137.5, self.x) + 12
            if other.x - 137.5 <= self.x <= other.x + 137.5:
                self.y = other.y + 20

        if group == 'ball:ground_q':
            self.on_ground = True
            if self.x < other.x - 62.5:
                self.x = max(other.x - 62.5, self.x) - 12
            if self.x > other.x + 62.5:
                self.x = min(other.x + 62.5, self.x) + 12
            if other.x - 62.5 <= self.x <= other.x + 62.5:
                self.y = other.y + 20

        if group == 'ball:wall':
            self.on_ground = True
            if self.x > other.x + 24:
                self.x = other.x + 24
            elif self.x < other.x - 24:
                self.x = other.x - 24
            else:
                self.x = clamp(other.x - 24, self.x, other.x + 24)
                self.y = other.y + 70

        if group == 'ball:bbl':
            self.on_ground = True
            if other.x - 16 <= self.x <= other.x + 16:
                self.y = other.y + 16

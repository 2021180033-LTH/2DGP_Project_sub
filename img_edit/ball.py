from pico2d import *

gr = 11
dirx, diry, VELOCITY, MASS = 0, 0, 5, 5


class Ball:
    def __init__(self):
        self.image = load_image("ball.png")
        self.x, self.y = 165, 200  # map1 xy
        self.x, self.y = 170, 346  # map2 xy
        self.x, self.y = 50, 490  # map3 xy
        self.frame = 0
        self.isJump = 0
        self.jump_progress_v, self.jump_g = 12, 1
        self.jump_last_v = -12
        self.jump_y = self.y

    def update(self):
        global dirx, diry
        self.x += dirx * 1.5
        if self.x > 800:
            self.x = 800
        elif self.x < 0:
            self.x = 0

        if self.isJump > 0:
            self.y += self.jump_progress_v
            self.jump_progress_v = self.jump_progress_v - self.jump_g

            if self.jump_last_v - 1 == self.jump_progress_v:
                self.jump(0)
                self.jump_progress_v = 12
        delay(0.015)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 25, 25, self.x, self.y)

    def jump(self, j):
        self.isJump = j

    def handle_event(self, event):
        global dirx, diry
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                 dirx += 1
            elif event.key == SDLK_LEFT:
                 dirx -= 1
            elif event.key == SDLK_UP:
                if self.isJump == 0:
                    self.jump(1)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                 dirx -= 1
            elif event.key == SDLK_LEFT:
                 dirx += 1

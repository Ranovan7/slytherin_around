from typing import List

import pygame
from pygame.locals import *
from pygame.math import Vector2

from games.platformers.master import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: List[int] = (400,400), size: int = 30):
        super().__init__()
        self.surf = pygame.Surface((size, size))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()

        self.pos = Vector2(pos)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)

        self.horizontal_limit = self.surf.get_width()/2

    def update(self):
        self.acc = Vector2(0,0)

        pressed_keys = pygame.key.get_pressed()

        self.process_input(pressed_keys)

        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.check_border()

        self.rect.midbottom = self.pos

    def process_input(pressed_keys):
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[K_UP]:
            self.acc.y = -ACC
        if pressed_keys[K_DOWN]:
            self.acc.y = ACC

    def check_border():
        if self.pos.x > WIDTH - self.horizontal_limit:
            self.pos.x = WIDTH - self.horizontal_limit
        if self.pos.x < self.horizontal_limit:
            self.pos.x = self.horizontal_limit
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y < self.surf.get_height():
            self.pos.y = self.surf.get_height()

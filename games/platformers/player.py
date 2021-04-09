from typing import List, Tuple

import pygame
from pygame.locals import *
from pygame.math import Vector2

from games.platformers.master import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple[int] = (400,400), size: int = 30):
        super().__init__()
        self.surf = pygame.Surface((size, size))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()

        self.position = Vector2(pos)
        self.velocity = Vector2(0,0)
        self.acceleration = Vector2(0,0)

        self.horizontal_limit = self.surf.get_width()/2

    def update(self):
        self.acceleration = Vector2(0,0)

        pressed_keys = pygame.key.get_pressed()

        self.process_input(pressed_keys)

        self.acceleration.x += self.velocity.x * FRIC
        self.acceleration.y += self.velocity.y * FRIC
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        self.check_border()

        self.rect.midbottom = self.position

    def process_input(self, pressed_keys: List):
        if pressed_keys[K_LEFT]:
            self.acceleration.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acceleration.x = ACC
        if pressed_keys[K_UP]:
            self.acceleration.y = -ACC
        if pressed_keys[K_DOWN]:
            self.acceleration.y = ACC

    def check_border(self):
        if self.position.x > WIDTH - self.horizontal_limit:
            self.position.x = WIDTH - self.horizontal_limit
        if self.position.x < self.horizontal_limit:
            self.position.x = self.horizontal_limit
        if self.position.y > HEIGHT:
            self.position.y = HEIGHT
        if self.position.y < self.surf.get_height():
            self.position.y = self.surf.get_height()

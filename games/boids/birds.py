from typing import List, Tuple

import pygame
from pygame.locals import *
from pygame.math import Vector2

from games.boids.master import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple[int] = (400,400), size: int = 10):
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
        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH
        if self.position.y > HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = HEIGHT


class Bird(pygame.sprite.Sprite):
    alignment_rad: float = 100.0
    cohesion_rad: float = 150.0
    separation_rad: float = 100.0
    min_speed: float = 10.0
    max_speed: float = 15.0
    acc_limit: float = 3.0

    def __init__(self, position: (int, int), id: int = None):
        self.position = position
        self.velocity = np.array([random.randint(-10.0, 10.0), random.randint(-10.0, 10.0)])
        self.acceleration = np.array([0.0, 0.0])
        self.id = id

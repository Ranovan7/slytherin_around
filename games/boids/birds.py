import random
from typing import List, Tuple

import pygame
from pygame.locals import *
from pygame.math import Vector2

from games.boids.master import *
from games.utils import euclidean_distance, set_mag, vec_clip


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
        self.position += self.velocity + self.acceleration

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
        super().__init__()

        self.position = Vector2(position)
        self.velocity = Vector2(random.randint(-10.0, 10.0), random.randint(-10.0, 10.0))
        self.acceleration = Vector2(0.0, 0.0)
        self.id = id

        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255,40,40))
        self.rect = self.surf.get_rect()

    def update(self):
        self.velocity += self.acceleration
        self.velocity = vec_clip(self.velocity, a_min=-self.max_speed, a_max=self.max_speed)
        self.position += self.velocity

        self.check_border()

        self.rect.midbottom = self.position
        self.acceleration = Vector2(0,0)

    def distance(self, bird):
        return euclidean_distance(self.position, bird.position)

    def emergence(self, birds):
        steer_align = Vector2(0, 0)
        steer_cohesion = Vector2(0, 0)
        steer_separation = Vector2(0, 0)
        count_align = 0
        count_cohesion = 0
        count_separation = 0

        for bird in birds:
            if bird == self:
                continue

            distance = self.distance(bird)
            if distance <= self.alignment_rad:
                count_align += 1
                steer_align = steer_align + bird.velocity

            if distance <= self.cohesion_rad:
                count_cohesion += 1
                steer_cohesion = steer_cohesion + bird.position

            if distance <= self.separation_rad:
                count_separation += 1
                diff = self.position - bird.position
                diff = Vector2(0, 0) if distance == 0 else diff / (distance * distance)
                steer_separation = steer_separation + diff

        if count_align > 0:
            steer_align = steer_align / count_align
            steer_align = set_mag(steer_align, self.min_speed)
            steer_align = steer_align - self.velocity

        if count_cohesion > 0:
            steer_cohesion = steer_cohesion / count_cohesion
            steer_cohesion = steer_cohesion - self.position
            steer_cohesion = set_mag(steer_cohesion, self.min_speed)
            steer_cohesion = steer_cohesion - self.velocity

        if count_separation > 0:
            steer_separation = steer_separation / count_separation
            steer_separation = set_mag(steer_separation, self.min_speed)
            steer_separation = steer_separation - self.velocity

        self.add_force(steer_align)
        self.add_force(steer_cohesion)
        self.add_force(steer_separation)

    def add_force(self, force):
        force = vec_clip(force, a_min=-self.acc_limit, a_max=self.acc_limit)
        self.acceleration = self.acceleration + force

    def check_border(self):
        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH
        if self.position.y > HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = HEIGHT

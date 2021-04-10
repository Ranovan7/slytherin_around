from typing import List, Tuple
import numpy as np
import random

import pygame
from pygame.math import Vector2

from games.bullet_hell.utils import get_vectors_angle, get_radians_from_points
from games.bullet_hell.master import *


class Bullet(pygame.sprite.Sprite):
    speed: int
    position: List[int]
    angle: int

    def __init__(self, position: Tuple[int], angle: int = 90):
        super().__init__()

        self.position = Vector2(position)
        self.velocity = Vector2(0,0)
        self.speed = 2
        self.angle = angle

        self.surf = pygame.Surface((15, 15))
        self.surf.fill((255,40,40))
        self.rect = self.surf.get_rect()

        self.width = self.surf.get_width()
        self.height = self.surf.get_height()

    def check_lifetime(self):
        if self.position.x > WIDTH + OUTER_LEN or self.position.x < -OUTER_LEN:
            self.kill()

        if self.position.y > HEIGHT + OUTER_LEN or self.position.y < -OUTER_LEN:
            self.kill()


class LinearBullet(Bullet):

    def update(self):
        self.check_lifetime()

        movement = get_vectors_angle(self.angle, FRIC)
        self.velocity.x += movement[0] * self.speed
        self.velocity.y += movement[1] * self.speed

        self.position += self.velocity

        self.rect.midbottom = self.position


class OscilatingBullet(Bullet):
    oscilation: int = 5
    upper_lim: int
    lower_lim: int

    def __init__(self, position: List[int], angle: int = 90):
        super().__init__(position, angle)

        self.upper_lim = angle + 40
        self.lower_lim = angle - 40

    def update(self):
        self.check_lifetime()

        movement = get_vectors_angle(self.angle, FRIC)
        self.velocity.x += movement[0] * self.speed
        self.velocity.y += movement[1] * self.speed

        self.position += self.velocity
        self.rect.midbottom = self.position

        self.angle += self.oscilation
        if self.angle >= self.upper_lim or self.angle <= self.lower_lim:
            self.oscilation *= -1


class TurningBullet(Bullet):
    angle_offset: int = 3
    offset_limit: int = 50

    def update(self):
        self.position = np.add(self.position, get_vectors_angle(self.angle, self.speed))
        if self.offset_limit > 0:
            self.angle += self.angle_offset
            self.offset_limit -= 1
        return self


class HomingBullet(Bullet):
    target: List[int]
    angle_diff_limit: int = 5

    def __init__(self, position: List[int], speed: int = 20, angle: int = 90):
        self.position = position
        self.speed = speed
        self.angle = angle

        self.target = np.array([position[0] - 400, position[1] - 400])

    def update(self):
        self.update_angle(get_radians_from_points(self.position, self.target))
        self.position = np.add(self.position, get_vectors_angle(self.angle, self.speed))
        return self

    def update_angle(self, radians):
        if self.angle == radians:
            return self

        cw = (self.angle - radians) % 360
        ccw = (radians - self.angle) % 360

        if cw <= self.angle_diff_limit or ccw <= self.angle_diff_limit:
            self.angle = radians
            return self

        if cw <= ccw:
            self.angle -= self.angle_diff_limit
        else:
            self.angle += self.angle_diff_limit

        return self

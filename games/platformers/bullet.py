from typing import List, Tuple
import numpy as np
import random

import pygame
from pygame.math import Vector2

from games.platformers.utils import get_vectors_angle, get_radians_from_points


class Bullet(pygame.sprite.Sprite):
    speed: int
    position: List[int]
    angle: int
    surf = pygame.Surface((10, 10))
    surf.fill((255,0,0))
    rect = surf.get_rect()

    def __init__(self, position: Tuple[int], speed: int = 10, angle: int = 90):
        self.position = Vector2(position)
        self.speed = speed
        self.angle = angle


class LinearBullet(Bullet):

    def update(self):
        self.position = np.add(self.position, get_vectors_angle(self.angle, self.speed))
        return self


class TurningBullet(Bullet):
    angle_offset: int = 3
    offset_limit: int = 50

    def update(self):
        self.position = np.add(self.position, get_vectors_angle(self.angle, self.speed))
        if self.offset_limit > 0:
            self.angle += self.angle_offset
            self.offset_limit -= 1
        return self


class OscilatingBullet(Bullet):
    oscilation: int = 5
    upper_lim: int
    lower_lim: int

    def __init__(self, position: List[int], speed: int = 20, angle: int = 90):
        self.position = position
        self.speed = speed
        self.angle = angle

        self.upper_lim = angle + 40
        self.lower_lim = angle - 40

    def update(self):
        self.position = np.add(self.position, get_vectors_angle(self.angle, self.speed))
        self.angle += self.oscilation

        if self.angle >= self.upper_lim or self.angle <= self.lower_lim:
            self.oscilation *= -1

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

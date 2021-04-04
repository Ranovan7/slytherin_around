from typing import List
import numpy as np

from bullets.utils import get_vectors_angle


class Bullet:
    speed: int
    position: List[int]
    angle: int

    def __init__(self, position: List[int], speed: int = 10, angle: int = 90):
        self.position = position
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
    lower_lim_lim: int

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

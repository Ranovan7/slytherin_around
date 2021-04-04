from typing import List
import numpy as np

from bullets.utils import get_vectors_angle


class Bullet:
    speed: int
    position: List[int]
    angle: int

    def __init__(self, position: List[int], speed: int = 20, angle: int = 90):
        self.position = position
        self.speed = speed
        self.angle = angle


class LinearBullet(Bullet):

    def update(self):
        self.position = np.add(self.position, get_vectors_angle(self.angle, self.speed))
        return self


class TurningBullet(Bullet):
    angle_offset: int = 3

    def update(self):
        self.position = np.add(self.position, get_vectors_angle(self.angle, self.speed))
        self.angle += self.angle_offset
        return self

from typing import List, Tuple
from collections.abc import Iterator
import numpy as np
import random
import math


def get_vectors_angle(angle: int, speed: int) -> List[List[int]]:
    movement = [
        speed * math.sin(math.radians(angle)),
        speed * math.cos(math.radians(angle))
    ]
    return movement


class BaseSpawner:
    speed: int = 20
    bullets: List[List[int]] = np.array([
        [0, -100],
        [0, 50],
        [0, 250],
        [0, 450],
        [0, 650],
        [0, 850],
        [0, 1050]
    ])

    def __init__(self, location: Tuple[int, int]):
        if random.randint(0,1) == 1:
            self.bullets = np.add(self.bullets, [1000, 0])
            self.speed = -20

    def update(self):
        self.bullets = np.add(self.bullets, [self.speed, 0])

    def get_frame(self) -> Tuple[List[int], List[int]]:
        return self.bullets


class CurveSpawner(BaseSpawner):
    rads: float = 0.0

    def update(self):
        self.bullets = np.add(self.bullets, [self.speed, get_vectors_angle(self.rads, self.speed)[1]])
        self.rads += 8


class BaseFireworks:
    speed: int = 20
    n_bullets: int = 8
    bullets: List[List[int]] = np.array([[0, 500]] * 8)
    angles: List[int] = np.array([
        0, 45, 90, 135, 180, 225, 270, 315
    ])

    def __init__(self, location: Tuple[int, int] = None):
        if location:
            self.bullets = np.array([location] * self.n_bullets)
        else:
            np.array([[0, 500]] * self.n_bullets)

    def update(self):
        self.bullets = np.add(self.bullets, [get_vectors_angle(angle, self.speed) for angle in self.angles])

    def get_frame(self) -> Tuple[List[int], List[int]]:
        return self.bullets

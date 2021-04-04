from typing import List, Tuple
from collections.abc import Iterator
import numpy as np
import math


def get_vectors_angle(angle: int, speed: int) -> List[List[int]]:
    movement = [
        speed * math.sin(math.radians(angle)),
        speed * math.cos(math.radians(angle))
    ]
    return movement


class BaseSpawner:
    speed: int = 10
    generator: Iterator = iter([])
    bullets: List[List[int]] = np.array([
        [0, 50],
        [0, 250],
        [0, 450],
        [0, 650],
        [0, 850]
    ])

    def __init__(self, location: Tuple[int, int]):
        pass

    def update(self):
        self.bullets = np.add(self.bullets, [20, 0])

    def get_frame(self) -> Tuple[List[int], List[int]]:
        return self.bullets


class CurveSpawner(BaseSpawner):
    count: float = 0.0
    vector: int = -10

    def update(self):
        self.bullets = np.add(self.bullets, [20, 2*self.vector])
        self.vector += 0.3


class BaseFireworks:
    bullets: List[List[int]] = np.array([[0, 500]] * 6)
    trajectory: List[List[int]] = np.array([
        [0, 20],
        [-10, 10],
        [-10, -10],
        [0, -20],
        [10, -10],
        [10, 10],
    ])
    angles: List[int] = np.array([
        0, 60, 120, 180, 240, 300
    ])

    def __init__(self, location: Tuple[int, int]):
        self.bullets = np.array([location] * 6)

    def update(self):
        self.bullets = np.add(self.bullets, [get_vectors_angle(angle, 20) for angle in self.angles])

    def get_frame(self) -> Tuple[List[int], List[int]]:
        return self.bullets

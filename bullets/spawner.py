from typing import List, Tuple
from collections.abc import Iterator
import numpy as np


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
        self.generator = self.behaviour(location)

    def behaviour(self, location: Tuple[int, int]) -> (List[int], List[int]):
        for i in range(100):
            self.update_bullets()
            yield self.bullets

    def update(self):
        self.update_bullets()

    def update_bullets(self):
        self.bullets = np.add(self.bullets, [20, 0])

    def get_frame(self) -> Tuple[List[int], List[int]]:
        return self.bullets


class CurveSpawner(BaseSpawner):
    count: float = 0.0

    def behaviour(self, location: Tuple[int, int]) -> (List[int], List[int]):
        for i in range(100):
            yield i**2

    def update_bullets(self):
        self.bullets = np.add(self.bullets, [20, 2*self.count])
        self.count += 0.5

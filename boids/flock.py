import random
import numpy as np
from typing import List


class Bird:
    position:(int, int)
    velocity:(int, int)
    acceleration:(int, int)

    def __init__(self, position: (int, int)):
        self.position = position
        self.velocity = np.array([random.randint(-10, 10), random.randint(-10, 10)])
        self.acceleration = np.array([0, 0])

    def update(self):
        self.position = np.add(self.position, self.velocity)
        self.velocity = np.add(self.velocity, self.acceleration)


class Flock:

    def __init__(
        self,
        n_birds: int = 30,
        border: int = 1000
    ):
        self.birds: List[(int, int)] = []
        for _ in range(n_birds):
            self.birds.append(
                Bird(np.array([random.randint(0, border), random.randint(0, border)]))
            )

    def update(self):
        for bird in self.birds:
            bird.update()

    def get_frame(self):
        return [bird.position for bird in self.birds]

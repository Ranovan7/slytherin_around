import random
import numpy as np
from typing import List

from boids.utils import euclidean_distance


class Bird:
    position:(int, int)
    velocity:(int, int)
    acceleration:(int, int)
    perception_rad: float = 100.0
    vel_limit: float = 10.0
    acc_limit: float = 1.0

    def __init__(self, position: (int, int)):
        self.position = position
        self.velocity = np.array([random.randint(-2.0, 2.0), random.randint(-2.0, 2.0)])
        self.acceleration = np.array([0.0, 0.0])

    def wrap(self, width, height):
        if self.position[0] > width:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = width

        if self.position[1] > height:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = height

    def update(self):
        self.position = np.add(self.position, self.velocity)
        self.velocity = np.clip(
            np.add(self.velocity, self.acceleration),
            a_min = -self.vel_limit,
            a_max = self.vel_limit)

    def align(self, birds: List):
        steering = np.array([0.0, 0.0])
        close = 0
        for bird in birds:
            if bird == self:
                continue

            if self.distance(bird) <= self.perception_rad:
                close += 1
                steering += np.add(steering, bird.velocity)

        if close > 0:
            steering = steering / close
            steering = np.subtract(steering, self.velocity)

        self.acceleration = np.clip(steering, a_min = -self.acc_limit, a_max = self.acc_limit)

    def distance(self, bird):
        return euclidean_distance(self.position, bird.position)


class Flock:

    def __init__(
        self,
        n_birds: int = 30,
        border: int = 1000
    ):
        self.birds: List[(int, int)] = []
        self.border = border
        for _ in range(n_birds):
            self.birds.append(
                Bird(np.array(
                    [
                        random.randint(0.0, float(border)),
                        random.randint(0.0, float(border))
                    ]
                ))
            )

    def update(self):
        for bird in self.birds:
            bird.wrap(self.border, self.border)
            bird.align(self.birds)
            bird.update()

    def get_frame(self):
        return [bird.position for bird in self.birds]
